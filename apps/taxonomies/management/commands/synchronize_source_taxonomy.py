# encoding: utf-8

from __future__ import unicode_literals

import logging
import os  # noqa: F401
import sys  # noqa: F401
import time  # noqa: F401
import traceback  # noqa: F401

from django.core.management.base import BaseCommand
from django.db import transaction
from lxml import etree  # noqa: F401
from taxonomies.models import Taxonomy, TaxonomyNode

log = logging.Logger("taxonomies.synchronize")


sources = {
    "AESGP": "Association Européenne des Spécialités Pharmaceutiques Grand Public",
}


class Command(BaseCommand):
    args = "none"
    help = "create source taxonomy"

    @transaction.atomic()
    def handle(self, *args, **options):
        taxonomy, _ = Taxonomy.objects.get_or_create(code="SOURCES")

        for src, sn in sorted(sources.items(), key=lambda x: (x[1], x[0])):
            tn, _ = TaxonomyNode.objects.get_or_create(code=src, taxonomy=taxonomy)
            tn.short_name = sn
            tn.extended_name = sn
            tn.save()
