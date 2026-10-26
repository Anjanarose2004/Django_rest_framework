from django.db import models

# Create your models here.
class MyModel(models.Model):
    title = models.CharField(max_length=100)
    language_choices=(
        ('en', 'English'),
        ('fr', 'French'),   
        ('ma','Malayalam'),
    )
    language = models.CharField(max_length=2, choices=language_choices)
    topic=models.CharField(max_length=100)
    note=models.TextField()
    