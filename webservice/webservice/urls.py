from django.conf.urls import include, url
from django.contrib import admin
from moviesoap.views import home, search_type, show_movie, add

urlpatterns = [
	url(r'^$', home, name='home'),
    url(r'^search/$', search_type, name='search'),
    url(r'^show/(\w+)/$', show_movie, name='show'),
    url(r'^add/$', add, name='add'),
]
