from django.conf.urls import patterns, url

from apps.shortener.views import home


urlpatterns = patterns('',
                       url(r'^/?$', home.home_page_view, name='home_page'),
)
