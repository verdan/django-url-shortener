from django.test import TestCase

from web.shortener.mangers import secret_words, tiny_urls


class TheSecretWordModelTests(TestCase):
    def setUp(self):
        self.secret_word = secret_words.create(slug='secret-word')

    def test_has_all_the_attributes(self):
        self.assertTrue(hasattr(self.secret_word, 'slug'))
        self.assertTrue(hasattr(self.secret_word, 'last_used'))
        self.assertTrue(hasattr(self.secret_word, 'is_consumed'))

    def test_is_consumed_flag_set_to_false_by_default(self):
        self.assertFalse(self.secret_word.is_consumed)

    def test_mark_as_consumed_invalidates_the_secret_word(self):
        self.assertFalse(self.secret_word.is_consumed)
        self.secret_word.mark_as_consumed()
        self.assertTrue(self.secret_word.is_consumed)


class TheTinyUrlModelTests(TestCase):
    def setUp(self):
        self.secret_word = secret_words.create(slug='secret-word', is_consumed=True)
        self.tiny_url = tiny_urls.create(belongs_to='http://www.google.com', linked_with=self.secret_word)

    def test_has_all_the_attributes(self):
        self.assertTrue(hasattr(self.tiny_url, 'belongs_to'))
        self.assertTrue(hasattr(self.tiny_url, 'linked_with'))
        self.assertTrue(hasattr(self.tiny_url, 'is_active'))
        self.assertTrue(hasattr(self.tiny_url, 'added_on'))
        self.assertTrue(hasattr(self.tiny_url, 'added_by'))

    def test_is_active_flag_set_to_true_by_default(self):
        self.assertTrue(self.tiny_url.is_active)

    def test_mark_as_inactive_invalidates_the_tiny_url(self):
        self.assertTrue(self.tiny_url.is_active)
        self.tiny_url.mark_as_inactive()
        self.assertFalse(self.tiny_url.is_active)
        self.assertFalse(self.tiny_url.linked_with)