from datetime import datetime

from libs.manager import Manager
from web.shortener.models import SecretWord, TinyUrl
from web.shortener.queries.secret_words import oldest_consumed_secret_word


class SecretWordManager(Manager):
    def get_oldest_consumed_secret_word(self):
        oldest_secret_word = self.get_first(oldest_consumed_secret_word)
        self.update(oldest_secret_word, last_used=datetime.now())
        tiny_urls.update(oldest_secret_word.tiny_url, is_active=False, linked_with=None)
        return oldest_secret_word


class TinyURLManager(Manager):
    pass


secret_words = SecretWordManager(SecretWord)
tiny_urls = TinyURLManager(TinyUrl)