from django.shortcuts import render
from django.http import HttpResponse
from store.models.category import Category
from store.models.products import Products
from store.models.category import Category

# Create your views here.
def index(request):
    content = dict()
    content['categories'] = Category.objects.all()
    products = Products.objects.all()
    content['products']=products
    return render(request,'index.html',content)