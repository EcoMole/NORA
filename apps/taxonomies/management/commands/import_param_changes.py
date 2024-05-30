# encoding: utf-8

from __future__ import unicode_literals

import logging

import pyexcel as pe
import pyexcel.ext.xlsx
from django.core.management import call_command  # noqa: F401
from django.core.management.base import BaseCommand
from django.db import connection, transaction
from taxonomies.models import Taxonomy, TaxonomyNode

log = logging.Logger("taxonomies.synchronize")


class Command(BaseCommand):
    args = "<efsa mapping file>"
    help = "Updates param taxonomy with efsa mapping file and performs sync with param taxonomy file"

    @transaction.atomic()
    def handle(self, *args, **options):
        if len(args) != 1:
            log.error(
                "Must be run with an efsa mapping file. "
                "Do not forget to import catalogue afterwards."
            )
            return

        taxonomy = Taxonomy.objects.get(code="PARAM")

        cursor = connection.cursor()

        sheet = pe.get_sheet(file_name=args[0])
        for row in range(1, 100000):
            our = sheet[row, 0]
            efsa = sheet[row, 1]

            if our is None:
                break

            if not our or not efsa:
                continue

            print(row, our, efsa)
            try:
                node = TaxonomyNode.objects.get(taxonomy=taxonomy, code=our)
                if (
                    TaxonomyNode.objects.filter(taxonomy=taxonomy, code=efsa).count()
                    > 0
                ):
                    print(
                        "Can not set mapping %s => %s - efsa taxonomy node already exists"
                        % (our, efsa)
                    )
                    continue

                cursor.execute(
                    "update taxonomies_taxonomynode set code=%s where id=%s",
                    (efsa, node.id),
                )
            except:  # noqa: E722
                if (
                    TaxonomyNode.objects.filter(taxonomy=taxonomy, code=efsa).count()
                    == 0
                ):
                    print("No taxonomy node found for our or efsa code", our, efsa)

        # call_command('synchronize_taxonomy_file', args[0])
        print("Done. Do not forget to import PARAM catalogue.")
