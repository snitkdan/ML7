from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    pub_date = models.DateField()
    publisher = models.CharField(max_length = 100)
    summary = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    purchase_link = models.URLField()
    cover_image = models.URLField()

class Author(models.Model):
    books = models.ManyToManyField(Book)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


