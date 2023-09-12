from django.db import models
from .category import Category
from django.utils.text import slugify
from django.urls import reverse

class Products(models.Model):
    name = models.CharField(max_length=254)
    original_price = models.IntegerField()
    sell_price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/')
    sku = models.CharField(max_length=254, blank=True)
    note = models.TextField(max_length=254,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product',kwargs={'slug':self.slug})

    def get_absolute_url_manager(self):
        return reverse('edit_product',kwargs={'slug':self.slug})