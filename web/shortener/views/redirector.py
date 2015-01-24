from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from libs.view import BaseView
from web.shortener.queries.tiny_urls import get_active_tiny_url_with_slug


class RedirectorView(BaseView):
    def get(self, slug):
        """
        Finds the Long URL against the shortified URL.
        Redirects to home page if not in database.
        """
        tiny_url = get_active_tiny_url_with_slug(linked_with_slug=slug)
        return redirect(tiny_url.belongs_to) if tiny_url else redirect(reverse('home_page'))


def redirector_view(request, slug):
    return RedirectorView(request).respond_with(slug)