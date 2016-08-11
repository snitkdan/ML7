from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from ratelimit.decorators import ratelimit

# Lists all books or create a new one
# books/

# ratelimit by ip address limiting gets/creates to 5/m
class BookList(generics.ListCreateAPIView):
    @ratelimit(key='ip', rate='5/m', method = ('GET', 'POST'), block=True)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Get a book, update it, or destroy it!
# books/pk
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

















