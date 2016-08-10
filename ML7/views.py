from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import Stock
from .models import Book
from .serializers import BookSerializer

# Lists all stocks or create a new one
# books/
class BookAuthList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)

    def post(self):
        pass




















from .models import Book
from .serializers import BookAuthSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class book_list(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAuthSerializer


class book_detail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookAuthSerializer

@api_view(('GET',))
def root(request, format=None):
    return Response({
        'books': reverse('book-list', request=request, format=format),
    })
