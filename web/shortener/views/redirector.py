from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from libs.queries import with_attrs
from libs.view import BaseView
from web.shortener.mangers import tiny_urls


class RedirectorView(BaseView):
    def get(self, slug):
        """
        Finds the Long URL against the shortified URL.
        Redirects to home page if not in database.
        """
        tiny_url = tiny_urls.get_first(with_attrs, is_active=True, linked_with__slug=slug)
        return redirect(tiny_url.belongs_to) if tiny_url else redirect(reverse('home_page'))


def redirector_view(request, slug):
    return RedirectorView(request).respond_with(slug)