from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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

















