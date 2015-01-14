from django.http import HttpResponse

from libs.view import BaseView


class HomePage(BaseView):
    template_name = 'shortener/home.html'

    def get(self, *args, **kwargs):
        return {}


def home_page_view(request):
    return HomePage(request).respond_with()