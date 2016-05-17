from django.conf.urls import url
from django.contrib import admin

#import view functions
from .views import (
	forum_list, 
	forum_detail,
	)

urlpatterns = [
	url(r'^$', forum_list, name='list'),
	url(r'^detail/(?P<id>\d+)/$', forum_detail, name='detail'),
]