from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.category import Category
from store.models.products import Products
from store.models.category import Category


def category(request,slug):
    content = dict()
    content['categories'] = Category.objects.all()
    category = Category.objects.get(slug = slug)
    products = Products.objects.filter(category=category)
    content['products'] = products
    return render(request, 'category.html', content)