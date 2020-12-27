from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    photo=models.ImageField(upload_to='images')

    def __str__(self): 
        return self.title 