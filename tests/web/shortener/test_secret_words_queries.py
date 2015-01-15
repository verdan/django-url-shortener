from datetime import datetime, timedelta

from django.test import TestCase

from web.shortener.mangers import secret_words, tiny_urls
from web.shortener.queries.secret_words import unconsumed_secret_word, oldest_consumed_secret_word


class TheUnConsumedSecretWordsQueryTests(TestCase):
    def setUp(self):
        self.secret_word_0 = secret_words.create(slug='dummy0')
        self.secret_word_1 = secret_words.create(slug='dummy1')

        yesterday = datetime.now() - timedelta(days=1)
        self.secret_word_2 = secret_words.create(slug='dummy2', last_used=yesterday, is_consumed=True)
        self.tiny_url_2 = tiny_urls.create(belongs_to='http://www.google.com/2/', linked_with=self.secret_word_2)

    def test_query_returns_word_related_to_the_url(self):
        url_to_shorten = u'http://www.google.com/dummy1/'
        secret_word = secret_words.get_first(unconsumed_secret_word, related_to_url=url_to_shorten)

        # Secret Word is matched with Available Related Secret Word.
        self.assertEqual(secret_word, self.secret_word_1)

    def test_query_returns_random_word_if_not_realated_to_url(self):
        url_to_shorten = u'http://www.google.com/dummmmmmmmmyyyyy/'
        secret_word = secret_words.get_first(unconsumed_secret_word, related_to_url=url_to_shorten)

        # Secret Word is Not Consumed
        self.assertFalse(secret_word.is_consumed)

        # Secret Word is Not Already Used Secret Word
        self.assertNotEqual(secret_word, self.secret_word_2)

        # Secret Word is a random available Secret Word
        self.assertIn(secret_word, [self.secret_word_0, self.secret_word_1])


class TheOldestConsumedSecretWordQueryTests(TestCase):
    def setUp(self):
        self.secret_word_1 = secret_words.create(slug='dummy1', is_consumed=True)
        self.tiny_url_1 = tiny_urls.create(belongs_to='http://www.google.com/dummy1/', linked_with=self.secret_word_1)
        self.secret_word_2 = secret_words.create(slug='dummy2', is_consumed=True)
        self.tiny_url_2 = tiny_urls.create(belongs_to='http://www.google.com/2/', linked_with=self.secret_word_2)

    def test_query_returns_oldest_consumed_secret_word(self):
        secret_word = secret_words.get_first(oldest_consumed_secret_word)

        # Secret Word is Consumed
        self.assertTrue(secret_word.is_consumed)

        # Secret Word is a Secret Word last used Yesterday.
        self.assertEqual(secret_word, self.secret_word_1)

