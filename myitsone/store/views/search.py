from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.products import Products
from store.models.category import Category
from store.models.search import Search


def search(request):
    content = dict()
    content['categories'] = Category.objects.all()
    if request.method == 'GET':
        search_item = request.GET['search']
        products = Products.objects.filter(name__icontains = search_item) | \
            Products.objects.filter(note__icontains=search_item)
        search =Search(name = search_item,result = len(products))
        search.save()
        content['products'] = products
        return render(request,'search.html',content)
    else:
        return redirect('index')
