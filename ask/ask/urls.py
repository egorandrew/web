from django.conf.urls import url,patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^$','qa.views.test'),
    url(r'^login/$','qa.views.test'),
    url(r'^signup/$','qa.views.test'),
    url(r'^guestion/\d+/$','qa.views.test'),
    url(r'^ask/$','qa.views.test'),
    url(r'^popular/$','qa.views.test'),
    url(r'^new/$','qa.views.test'),
]
