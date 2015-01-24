from libs.view import BaseView
from web.shortener.forms.url_shortner_form import UrlShortenerForm
from web.shortener.presenters import TinyUrlPresenter
from web.shortener.queries.secret_words import unconsumed_secret_word, oldest_consumed_secret_word
from web.shortener.queries.tiny_urls import get_active_tiny_url_with_belongs_to, create_tiny_url


class HomePageView(BaseView):
    template_name = 'shortener/home.html'

    @staticmethod
    def retrieve_available_secret_word(for_url):
        """
        Finds the appropriate secret word against given URL.
        Returns unconsumed secret word if found, else find the oldest secret word used.
        """
        available_word = unconsumed_secret_word(related_to_url=for_url)
        if not available_word:
            available_word = oldest_consumed_secret_word()
        available_word.mark_as_consumed()
        return available_word

    def create_new_shortened_url(self, long_url_of_user):
        secret_word = self.retrieve_available_secret_word(for_url=long_url_of_user)
        if secret_word:
            return create_tiny_url(belongs_to=long_url_of_user, linked_with=secret_word)


    def get_context_data(self, **kwargs):
        """
        Returns the data that needs to be rendered on the frontend.
        """
        long_url_of_user = kwargs.get('long_url_of_user').lower()
        already_shortened = get_active_tiny_url_with_belongs_to(belongs_to=long_url_of_user)
        shortened_url = already_shortened or self.create_new_shortened_url(long_url_of_user)

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