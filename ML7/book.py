from django.db import models
from django.utils import timezone

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length = 100)
  pub_date = models.DateField()
  publisher = models.CharField(max_length = 100)
  summary = models.CharField(max_length = 1000)
  price = models.DecimalField(max_digits = 5, decimal_places = 2)
  purchase_link = models.URLField()
  cover_image = models.URLField()
