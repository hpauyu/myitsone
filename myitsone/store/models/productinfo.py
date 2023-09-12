from django.db import models
from .products import Products


class ProductInfo(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment = models.CharField(max_length=254)
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)