from django.db import models

# Create your models here.

class BookDB(models.Model):
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    GENRE_CHOICES = (
        ('fi', 'Fiction'),
        ('sc', 'Science'),
        ('hi', 'History'),
    )
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    price = models.IntegerField()
    published_year = models.IntegerField()
    description = models.TextField()

