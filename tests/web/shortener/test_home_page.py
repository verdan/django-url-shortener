from django.core.urlresolvers import reverse

from django.test import TestCase, RequestFactory

from web.shortener.mangers import secret_words, tiny_urls
from web.shortener.views.home import HomePageView


class TheHomePagetTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()

    def test_returns_the_url_shortner_form(self):
        request = self.request.get(reverse('home_page'))
        context = HomePageView(request).get()

        # Context has the Shortener Form
        self.assertTrue(context['shortener_form'])


class TheHomePageSubmissionTests(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.secret_word_1 = secret_words.create(slug='dummy1', is_consumed=True)
        self.tiny_url_1 = tiny_urls.create(belongs_to='http://www.google.com/dummy1/', linked_with=self.secret_word_1)
        self.secret_word_2 = secret_words.create(slug='dummy2')
        self.secret_word_3 = secret_words.create(slug='dummy3')

    def test_returns_the_shortified_url(self):
        url_to_shorten = 'http://www.google.com/dummy2/'
        request = self.request.post(reverse('home_page'), data={'url': url_to_shorten})
        context = HomePageView(request).post()

        # Context has the Shortener Form
        self.assertTrue(context['shortener_form'])

        # Context has the Longer Version of the URL
        self.assertTrue(context['long_url_of_user'])

        # URL not already shortened.
        self.assertFalse(context['already_shortened'])

        self.assertEqual(context['shortened_url']._item.linked_with, self.secret_word_2)

    def test_returns_already_shortified_error(self):
        request = self.request.post(reverse('home_page'), data={'url': self.tiny_url_1.belongs_to})
        context = HomePageView(request).post()

        # URL already shortened.
        self.assertTrue(context['already_shortened'])