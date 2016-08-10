from rest_framework import serializers
from .models import Book, Author

class BookAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'