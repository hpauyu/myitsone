from django.db import models
from .category import Category


class Search(models.Model):
    name = models.CharField(max_length=254)
    result = models.IntegerField()