# encoding: utf-8

from __future__ import unicode_literals

import logging
import os
import sys
import time
import traceback  # noqa: F401
from collections import Counter
from itertools import groupby

from django.core.management.base import BaseCommand, CommandError
from django.db import connection, transaction
from lxml import etree
from taxonomies.models import ImplicitAttribute, Taxonomy, TaxonomyNode

from utils.sync_mixin import SyncMixin  # noqa: F401

log = logging.getLogger("taxonomies.synchronize")


def ct(element, child_name):
    r = element.xpath(child_name)
    if len(r) == 0:
        return None
    return r[0].text


def get_taxonomy_path(element):
    r = []
    while element:
        r.append("%s[%s]" % (element.code, element.order))
        element = element.parent
    r.reverse()
    return "/".join(r)


class UnknownParentError(Exception):
    pass


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("filename", nargs="+", type=str)

        # Named (optional) arguments
        parser.add_argument(
            "--remove-deleted",
            action="store_true",
            dest="remove_deleted",
            default=False,
            help="If used, mark the taxonomy nodes that "
            "were not found in the new taxonomy as deprecated",
        )

        parser.add_argument(
            "--chunk-size",
            type=int,
            dest="chunk_size",
            default=10000,
            help="If used, sets the number of characters to be read from the file at the time.",
        )

        help = "Reads in taxonomy file"  # noqa F841

    def parse_and_call(self, fname, chunk_size):
        parser = etree.XMLPullParser(events=("end",))
        catalogue_code = None
        delayed_records = []
        try:
            with open(fname) as f:
                while True:
                    data = f.read(chunk_size)
                    if not data:
                        break

                    parser.feed(data)

                    for action, element in parser.read_events():
                        if element.tag == "catalogueDesc":
                            catalogue_code = ct(element, "code")
                            self.taxonomy, _ = Taxonomy.objects.get_or_create(
                                code=catalogue_code
                            )
                            print(
                                "Catalogue code %s, taxonomy pk %s"
                                % (catalogue_code, self.taxonomy.pk)
                            )
                            self.load_taxonomy()
                            element.clear()

                        elif element.tag == "term":
                            term_code = ct(element, "termDesc/termCode")
                            term_extended_name = ct(
                                element, "termDesc/termExtendedName"
                            )
                            term_scope = ct(element, "termDesc/termScopeNote")
                            status = ct(element, "termVersion/status")
                            assignments = element.xpath(
                                "hierarchyAssignments/hierarchyAssignment"
                            )
                            attributes = element.xpath(
                                "implicitAttributes/implicitAttribute"
                            )

                            reportable = None
                            for a in assignments:
                                reportable_str = ct(a, "reportable")
                                if reportable_str == "true":
                                    reportable = True
                                elif reportable_str == "false" and reportable is None:
                                    reportable = False

                            if reportable is None:
                                reportable = True

                            is_botanic = False
                            is_yesno = False
                            is_gender = False
                            is_part_nature = False
                            is_process = False

                            for a in assignments:
                                reportable_str = ct(a, "reportable")
                                hc = ct(a, "hierarchyCode")
                                if hc == "YESNO" and reportable_str == "true":
                                    is_yesno = True
                                    break
                                if hc == "gender" and reportable_str == "true":
                                    is_gender = True
                                    break
                                if hc == "part" and reportable_str == "true":
                                    is_part_nature = True
                                    break
                                if hc == "process" and reportable_str == "true":
                                    is_process = True
                                    break

                            if len(assignments) > 1:
                                # need to get the right assignement
                                assignment = None
                                for a in assignments:
                                    hc = ct(a, "hierarchyCode")
                                    if hc == "botanic":
                                        assignment = a
                                        is_botanic = True
                                        break  # we have all we need: assignment and is_botanic
                                    elif hc == catalogue_code:
                                        assignment = a

                                if assignment is None:
                                    raise Exception(
                                        "Do not have hierarchy code for %s"
                                        % catalogue_code
                                    )
                            else:
                                assignment = assignments[0]

                            attrs = {}
                            for attribute in attributes:
                                code = attribute.xpath("attributeCode")[0].text
                                if code not in attrs:
                                    attrs[code] = []
                                for val in attribute.xpath(
                                    "attributeValues/attributeValue"
                                ):
                                    attrs[code].append(val.text)

                            parent_code = ct(assignment, "parentCode")
                            try:
                                order = int(ct(assignment, "order"))
                            except:  # noqa: E722
                                order = 0

                            try:
                                self.sync_node(
                                    term_code,
                                    term_extended_name,
                                    term_scope,
                                    status,
                                    parent_code,
                                    order,
                                    attrs,
                                    reportable,
                                    is_botanic,
                                    is_yesno,
                                    is_gender,
                                    is_part_nature,
                                    is_process,
                                )
                            except UnknownParentError:
                                log.warning(
                                    "\nUnknown parent '%s' for '%s', storing record for "
                                    "later processing",
                                    parent_code,
                                    term_code,
                                )
                                delayed_records.append(
                                    (
                                        term_code,
                                        term_extended_name,
                                        term_scope,
                                        status,
                                        parent_code,
                                        order,
                                        attrs,
                                        reportable,
                                        is_botanic,
                                        is_yesno,
                                        is_gender,
                                        is_part_nature,
                                        is_process,
                                    )
                                )
        finally:
            parser.close()
        while delayed_records:
            last_loop_records = len(delayed_records)
            log.warning("\nProcessing %d delayed records", len(delayed_records))
            new_delayed = []
            for rec in delayed_records:
                try:
                    self.sync_node(*rec)
                except UnknownParentError:
                    new_delayed.append(rec)
            delayed_records = new_delayed
            if "root" in [rec[4] for rec in delayed_records]:
                # root node is missing, let's add it
                log.info(
                    f'Automatically adding root node for taxonomy "{self.taxonomy}"'
                )
                node = TaxonomyNode.objects.create(
                    taxonomy=self.taxonomy,
                    code="root",
                    short_name="root",
                    extended_name="root",
                )
                self.code_to_node["root"] = node
            elif len(delayed_records) >= last_loop_records:
                log.error(
                    "The number of delayed records is not getting lower with more "
                    "iterations as it should, stopping. Probably some parent element is "
                    "missing completely - check that the 'root' element for the taxonomy "
                    "exists if adding a new taxonomy"
                )
                break

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.taxonomy = None
        self.code_to_node = {}
        self.seen_codes = set()
        self.stats = Counter()
        self.iattrs = {}

    def load_taxonomy(self):
        self.code_to_node = {
            node.code: node
            for node in TaxonomyNode.objects.filter(taxonomy=self.taxonomy)
        }
        self.seen_codes = set()
        self.iattrs = {
            node_id: list(group)
            for node_id, group in groupby(
                ImplicitAttribute.objects.filter(node__taxonomy=self.taxonomy).order_by(
                    "node_id", "code", "value"
                ),
                key=lambda x: x.node_id,
            )
        }

    def sync_node(
        self,
        term_code,
        term_extended_name,
        term_scope,
        status,
        parent_code,
        order,
        implicit_attributes,
        reportable,
        is_botanic,
        is_yesno,
        is_gender,
        is_part_nature,
        is_process,
    ):
        # handle status
        if status == "APPROVED":
            status = TaxonomyNode.STATUS.APPROVED
        elif status == "DEPRECATED":
            status = TaxonomyNode.STATUS.DEPRECATED
        elif status == "PRELIMINARY":
            status = TaxonomyNode.STATUS.PRELIMINARY
        else:
            raise Exception("Unhandled status %s" % status)

        # node attrs
        if parent_code and parent_code not in self.code_to_node:
            raise UnknownParentError()
        parent_id = self.code_to_node[parent_code].pk if parent_code else None
        params = dict(
            code=term_code,
            taxonomy_id=self.taxonomy.pk,
            parent_id=parent_id,
            extended_name=term_extended_name,
            status=status,
            reportable=reportable,
            order=order,
            scope=term_scope,
            is_botanic=is_botanic,
            is_yesno=is_yesno,
            is_gender=is_gender,
            is_part_nature=is_part_nature,
            is_process=is_process,
        )

        # sync or create
        node = self.code_to_node.get(term_code)
        if node:
            save = False
            for key, value in params.items():
                if getattr(node, key) != value:
                    setattr(node, key, value)
                    save = True
            if save:
                node.save()
                self.stats["synced"] += 1
            else:
                self.stats["unchanged"] += 1
        else:
            node = TaxonomyNode.objects.create(**params)
            self.code_to_node[term_code] = node
            self.stats["created"] += 1

        # implicit attributes
        # attrs = node.implicit_attributes.all().order_by('code', 'value')
        attrs = self.iattrs.get(node.pk) or []
        lattrs = {}
        for attr in attrs:
            if attr.code not in lattrs:
                lattrs[attr.code] = []
            lattrs[attr.code].append(attr)

        for new_attr_code, new_attr_vals in implicit_attributes.items():
            modify = False
            local_vals = []

            if new_attr_code not in lattrs:
                modify = True
            else:
                local_vals = lattrs[new_attr_code]
                del lattrs[new_attr_code]

                new_attr_vals.sort()
                if len(new_attr_vals) != len(local_vals):
                    modify = True
                else:
                    for vi in range(len(new_attr_vals)):
                        if local_vals[vi] != new_attr_vals[vi]:
                            modify = True
                            break
            if modify:
                # self.stats['ia modify'] += 1
                # remove old unmatching values
                seen_values = set()
                for val in local_vals:
                    if val.value not in new_attr_vals:
                        val.delete()
                    else:
                        seen_values.add(val.value)

                # create new values
                for val in new_attr_vals:
                    if val not in seen_values:
                        ImplicitAttribute.objects.create(
                            node=node, code=new_attr_code, value=val
                        )
                        self.stats["ia create"] += 1

        # remove old codes (local which are not in implicit_attributes)
        for local_vals in lattrs.values():
            for val in local_vals:
                val.delete()
                self.stats["ia delete"] += 1

        # print stats
        if sum(self.stats.values()) % 10 == 0:
            sys.stdout.write(
                "\rstats: {}; queries: {}".format(self.stats, len(connection.queries))
            )
            sys.stdout.flush()

    @transaction.atomic()
    def handle(self, *__args, **options):
        if options["remove_deleted"]:
            raise CommandError(
                "Removing of nodes no longer present in the tree is not supported"
            )

        stime = time.time()
        for fname in options["filename"]:
            print("Parsing", fname)
            if os.path.getsize(fname) > 1000000:
                log.warning("File larger than 1 MB, using delayed MPTT sync")
                with TaxonomyNode.objects.disable_mptt_updates():
                    self.parse_and_call(fname, chunk_size=options["chunk_size"])
                if set(self.stats.keys()) != {"unchanged"}:
                    # rebuild only if there was some change
                    TaxonomyNode.objects.rebuild()
            else:
                with TaxonomyNode.objects.delay_mptt_updates():
                    self.parse_and_call(fname, chunk_size=options["chunk_size"])
        etime = time.time()

        print("    update took %s seconds" % (int(etime - stime)))
        print("{} db queries made".format(len(connection.queries)))
