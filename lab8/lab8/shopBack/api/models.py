from django.db import models

from django.http import JsonResponse
from django.views import View
from django.urls import path

class Category(models.Model):
    name =  models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categpries"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name
    