from django.conf.urls import patterns, url

from web.shortener.views import home, redirector


urlpatterns = patterns('',
                       url(r'^(?P<slug>\w+)/?$', redirector.redirector_view, name='redirector'),
                       url(r'^/?$', home.home_page_view, name='home_page'),

)
