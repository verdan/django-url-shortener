from libs.manager import Manager
from web.shortener.models import SecretWord, TinyUrl


class SecretWordManager(Manager):
    pass


class TinyURLManager(Manager):
    pass


secret_words = SecretWordManager(SecretWord)
tiny_urls = TinyURLManager(TinyUrl)