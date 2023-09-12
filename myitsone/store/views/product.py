from django.shortcuts import render
from django.http import HttpResponse
from store.models.products import Products
from store.models.category import Category


def product(request,slug):
    content =dict()
    content['categories'] = Category.objects.all()
    product = Products.objects.get(slug = slug)
    content['product'] = product
    return render(request,'product.html',content)