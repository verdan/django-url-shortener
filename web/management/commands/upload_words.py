from django.core.management.base import NoArgsCommand
import os

class Command(NoArgsCommand):
    help = 'Uploads Words in Database'

    def _header(self, message, is_title=False):
        self.stdout.write('%s %s %s' % ((is_title and '#' or '>') * 20, message, (is_title and '#' or '<') * 20))

    def handle_noargs(self, **options):
        dev_null = open(os.devnull, 'w')
        self._header(self.help)