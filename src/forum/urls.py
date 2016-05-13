from django.conf.urls import url
from django.contrib import admin

#import view functions
from .views import (
	forum_list, 
	)

urlpatterns = [
	url(r'^$', forum_list, name='list'),
]