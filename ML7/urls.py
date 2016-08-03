from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from ML7 import views

urlpatterns = [
  url(r'^$', views.root),
  url(r'books/$', views.book_list.as_view(), name='book-list'),
] 

