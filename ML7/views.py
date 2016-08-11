from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import UserRateThrottle

# Lists all books or create a new one
# books/

# ratelimit by ip address limiting gets/creates to 5/m
class BookList(generics.ListCreateAPIView):
    throttle_classes = (UserRateThrottle,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Get a book, update it, or destroy it!
# books/pk
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

















