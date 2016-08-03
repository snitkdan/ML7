from .book import Book
from .serializers import BookAuthSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse 

# Create your views here.
class book_list(generics.ListCreateAPIView):
  #API endpoint that allows users to be viewed
  queryset = Book.objects.all()
  serializer_class  = BookAuthSerializer

@api_view(('GET',))
def root(request, format = format):
  return Response({
    'books': reverse('book-list', request = request, format = format),
  })
