from django.shortcuts import render,redirect
from django.http import HttpResponse
from decorators import authenticated_manager
from forms import Product
from store.models.products import Products
from store.models.inventory import Inventory
from account.models.orderitems import OrderItems
from account.models.orderdetail import OrderDetail
from django.db.models import Q


@authenticated_manager
def all_products(request):
    content = dict()
    product_list = list()
    products = Products.objects.all()
    for product in products:
        data = dict()
        data['name'] = product.name
        data['profit'] = ((product.sell_price -product.original_price)/product.original_price)*100
        data['inventory'] = Inventory.objects.get(product = product).quantity
        items =OrderItems.objects.filter(product=product)
        x = 0
        for item in items:
            if item.order.order_status == 'Completed':
                x += 1
        data['sold'] = x
        data['remaining'] = data['inventory'] - data['sold']
        data['url'] = product.get_absolute_url_manager
        product_list.append(data)
    content['products'] = product_list
    return render(request,'manager/all-products.html',content)