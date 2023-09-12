from django.db import models
from .products import Products

class Inventory(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)