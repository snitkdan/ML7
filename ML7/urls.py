from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ML7 import views

urlpatterns = [
    url(r'^$', views.BookList.as_view(), name='book-list'),
    #url(r'^(?P<pk>[0-9]+)/$', views.BookDetail.as_view(), name='book-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
