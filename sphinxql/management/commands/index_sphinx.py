from __future__ import unicode_literals

import sys
from django.core.management.base import BaseCommand

from sphinxql import configuration


class Command(BaseCommand):
    help = "Indexes your models."

    def add_arguments(self, parser):
        parser.add_argument(
            '--update',
            action='store_true',
            help='',
            default=False)

    def handle(self, **options):
        self.stdout.write('Started indexing')
        self.stdout.write('----------------')

        if options['update']:
            configuration.reindex(output=sys.stdout)
        else:
            configuration.index(output=sys.stdout)

        self.stdout.write('-----------------')
        self.stdout.write('Indexing finished')
