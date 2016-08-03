from django.db import models
from ML7.book import Book

class Author(models.Model):
  f_name = models.CharField(max_length = 50)
  l_name = models.CharField(max_length = 50)
  books = models.ManyToManyField(Book)


