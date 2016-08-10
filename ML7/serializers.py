from rest_framework import serializers
from .models import Book

class BookAuthSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ('id', 'title', 'pub_date', 'publisher', 'summary', 'price', 'purchase_link', 'cover_image')


