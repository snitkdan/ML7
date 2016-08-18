from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.throttling import UserRateThrottle

#Default rate limit = 10/m

# Lists all books or create a new one
# books/

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Get a book, update it, or destroy it!
# books/pk
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

















