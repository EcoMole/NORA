# encoding: utf-8

from __future__ import unicode_literals

import fnmatch
import logging
import os

from django.core.management import call_command
from django.core.management.base import BaseCommand

log = logging.Logger("taxonomies.synchronize")


class Command(BaseCommand):
    help = "Reads all taxononomy files in the directory (recursively) and updates taxonomies"

    def add_arguments(self, parser):
        parser.add_argument("path_to_taxonomy_directory", type=str)

    def handle(self, *args, **options):
        # traverse root directory, and list directories as dirs and files as files
        for root, dirs, files in os.walk(options["path_to_taxonomy_directory"]):
            for file in fnmatch.filter(files, "*.xml"):
                file = os.path.join(root, file)
                print(file)

                call_command("synchronize_taxonomy_file", file)
