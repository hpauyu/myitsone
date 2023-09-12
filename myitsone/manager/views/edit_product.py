from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.products import Products
from store.models.inventory import Inventory
from forms import Product
from decorators import authenticated_manager


@authenticated_manager
def edit_product(request,slug):
    product = Products.objects.get(slug=slug)
    inventory = Inventory.objects.get(product = product)
    initial = dict()
    initial['name']=product.name
    initial['original_price'] =product.original_price
    initial['sell_price']=product.sell_price
    initial['category']=product.category
    initial['image'] = product.image
    initial['sku'] = product.sku
    initial['note'] = product.note
    initial['quantity'] = inventory.quantity
    product_form = Product(initial=initial)
    if request.method == 'POST':
        product_form = Product(request.POST, request.FILES)
        try:
            product_form.is_valid()
            product.name= product_form.cleaned_data['name']

            product.original_price=product_form.cleaned_data['original_price']
            product.sell_price=product_form.cleaned_data['sell_price']
            product.category= product_form.cleaned_data['category']
            product.sku = product_form.cleaned_data['sku']
            product.note = product_form.cleaned_data['note']
            product.save()
            inventory.quantity = product_form.cleaned_data['quantity']
            inventory.save()
        except:
            pass
        return redirect('manager')

    return render(request,'manager/edit-product.html',{'form':product_form})