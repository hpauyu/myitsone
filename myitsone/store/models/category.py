from django.db import models
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=254,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=False,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category',kwargs={'slug':self.slug})