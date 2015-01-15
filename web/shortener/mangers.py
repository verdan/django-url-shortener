from libs.manager import Manager
from web.shortener.models import SecretWord, TinyUrl
from web.shortener.queries.secret_words import oldest_consumed_secret_word


class SecretWordManager(Manager):
    def get_oldest_consumed_secret_word(self):
        """
        Finds the Oldest Consumed Secret Word.
        Updates the last Used time of the Secret Word.
        Un-links the Tiny URL associated with that Secret Word
        """
        oldest_secret_word = self.get_first(oldest_consumed_secret_word)
        oldest_secret_word.mark_as_consumed()
        oldest_secret_word.tiny_url.mark_as_inactive()
        return oldest_secret_word


class TinyURLManager(Manager):
    pass


secret_words = SecretWordManager(SecretWord)
tiny_urls = TinyURLManager(TinyUrl)