from django.shortcuts import render,redirect
from django.http import HttpResponse
from decorators import authenticated_manager
from forms import Product
from store.models.products import Products
from store.models.inventory import Inventory


@authenticated_manager
def add_product(request):
    content =dict()
    if request.method =="POST":
        product_form = Product(request.POST,request.FILES)
        try:
            product_form.is_valid()
            name = product_form.cleaned_data['name']
            original_price = product_form.cleaned_data['original_price']
            sell_price = product_form.cleaned_data['sell_price']
            category = product_form.cleaned_data['category']
            image = product_form.cleaned_data['image']
            sku = product_form.cleaned_data['sku']
            note = product_form.cleaned_data['note']
            new_product = Products(name = name,
                                   original_price=original_price,
                                   sell_price=sell_price,
                                   category=category,
                                   image =image,
                                   sku =sku,
                                   note= note)
            new_product.save()
            quantity = product_form.cleaned_data['quantity']
            inventory = Inventory(product = new_product, quantity=quantity)
            inventory.save()
        except:
            pass


    content['form'] = Product
    return render(request,'manager/add-product.html',content)