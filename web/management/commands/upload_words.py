from django.core.management.base import NoArgsCommand
from django.conf import settings
from django.utils.text import slugify

from web.shortener.mangers import secret_words

from web.shortener.models import SecretWord


FILE_PATH = '%s/words.txt' % settings.FIXTURES_PATH


class Command(NoArgsCommand):
    help = 'Uploads Words in Database'

    def _header(self, message, is_title=False):
        self.stdout.write('%s %s %s' % ((is_title and '#' or '>') * 20, message, (is_title and '#' or '<') * 20))

    def handle_noargs(self, **options):
        self._header(self.help)
        try:
            secret_words_list = []
            words = open(FILE_PATH).read().splitlines()
            existing_secret_words = secret_words.flat_values_list(secret_words.all(), field='slug')
            for word in set(words):
                slugify_word = slugify(unicode(word))
                if not word in existing_secret_words:
                    secret_words_list.append(SecretWord(slug=slugify_word))
            secret_words.bulk_create(secret_words_list)
        except IOError:
            print "No Words File detected. Please try again after placing words.txt in the fixtures directory."