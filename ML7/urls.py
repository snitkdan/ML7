from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ML7 import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^books/$', views.book_list.as_view(), name='book-list'),
    #url(r'^books/(?P<pk>[0-9]+)/$', views.Book_detail.as_view(), name='Book_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
