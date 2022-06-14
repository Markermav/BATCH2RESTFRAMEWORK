from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=280, unique=True)
    price = models.IntegerField()
    image = models.CharField(max_length=280)

    def __str__(self):
        return f'{self.id} : {self.name}'

