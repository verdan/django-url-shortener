from libs.queries import with_attrs
from libs.view import BaseView
from web.shortener.forms.url_shortner_form import UrlShortenerForm
from web.shortener.mangers import secret_words, tiny_urls
from web.shortener.presenters import TinyUrlPresenter
from web.shortener.queries.secret_words import unconsumed_secret_word


class HomePageView(BaseView):
    template_name = 'shortener/home.html'

    @staticmethod
    def retrieve_available_secret_word(for_url):
        available_word = secret_words.get_first(unconsumed_secret_word, related_to_url=for_url)
        if not available_word:
            available_word = secret_words.get_oldest_consumed_secret_word()
        secret_words.update(available_word, is_consumed=True)
        return available_word


    def get_context_data(self, **kwargs):
        long_url_of_user = kwargs.get('long_url_of_user').lower()
        already_shortened = tiny_urls.get_first(with_attrs, belongs_to=long_url_of_user, is_active=True)
        if already_shortened:
            shortened_url = already_shortened
        else:
            secret_word = self.retrieve_available_secret_word(for_url=long_url_of_user)
            shortened_url = tiny_urls.create(belongs_to=long_url_of_user, linked_with=secret_word)

        return super(HomePageView, self).get_context_data(already_shortened=True if already_shortened else False,
                                                          shortened_url=TinyUrlPresenter(shortened_url, self.request),
                                                          **kwargs)

    def get(self):
        return {'shortener_form': UrlShortenerForm()}

    def post(self):
        shortener_form = UrlShortenerForm(self.request.POST)
        if not shortener_form.is_valid():
            return {'shortener_form': shortener_form}

        long_url_of_user = shortener_form.cleaned_data.get('url')
        return self.get_context_data(shortener_form=shortener_form, long_url_of_user=long_url_of_user)


def home_page_view(request):
    return HomePageView(request).respond_with()