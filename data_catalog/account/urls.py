__author__ = 'mstacy'
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'get_apikey/', 'account.views.get_apikey'),
)
