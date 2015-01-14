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

    @staticmethod
    def get_unique_words_from_file():
        """
        Reads the file placed in the fixtures directory and returns the Set of slug of each word in the file.
        Why Set ? So that we can make calculations on these slugs.
        """
        words_from_files = open(FILE_PATH).read().splitlines()

        def slugify_word(value):
            return slugify(unicode(value))

        return set(map(slugify_word, words_from_files))

    @staticmethod
    def get_existing_secret_words():
        """
        Returns Set of slugs of existing secret words in the database.
        """
        existing_words = secret_words.all()
        return set(secret_words.flat_values_list(existing_words, field='slug'))

    @staticmethod
    def get_words_to_add(words_from_file, existing_words):
        """
        Returns the list of filtered words that we actually need to load in the database by subtracting
        the existing words from the newly got words form the file.
        """
        return list(words_from_file - existing_words)

    def handle_noargs(self, **options):
        self._header(self.help)
        words_from_file = []
        insertion_list = []
        try:
            words_from_file = self.get_unique_words_from_file()
        except IOError:
            print "No Words File detected. Please try again after placing words.txt in the fixtures directory."

        existing_secret_words = self.get_existing_secret_words()
        filtered_words = self.get_words_to_add(words_from_file, existing_secret_words)

        for word in filtered_words:
            insertion_list.append(SecretWord(slug=word))

        secret_words.bulk_create(insertion_list)

        if filtered_words:
            success_message = 'Hurray! %d words loaded in the database successfully.' % len(filtered_words)
        else:
            success_message = 'Nothing seems to have changed. All the words in the file already exist in the system.'

        print success_message