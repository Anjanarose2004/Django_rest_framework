from rest_framework import serializers
from myapp.models import BookDB

class BookDbserializer(serializers.Serializer):
    book_name=serializers.CharField(max_length=150)
    author=serializers.CharField(max_length=100)
    genre=serializers.CharField(max_length=100)
    price=serializers.IntegerField()
    published_year=serializers.IntegerField()
    description=serializers.CharField()