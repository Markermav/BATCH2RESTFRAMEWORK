from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=280)
    price = serializers.IntegerField()
    image = serializers.CharField(max_length=280)

    def create (self, validate_data):
        return Book.objects.create(**validate_data)

    
    def update(self, instance, validate_data):
        instance.price = validate_data.get('price', instance.price)
        instance.image = validate_data.get('image', instance.image)
        instance.save()
        return instance
    

