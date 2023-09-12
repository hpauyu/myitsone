from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models.account import Account
from store.models.cart import Cart
from store.models.products import Products
from django.core.exceptions import ObjectDoesNotExist


def editCart(request):
    if request.method == 'GET':
        info = request.GET
        key = list(info.keys())
        if 'user' in request.session:
            account = Account.get_account_by_id(request.session['user'])
            for name in key:
                if 'removeProduct' in name:
                    try:
                        product_name = Products.objects.get(name=info[name])
                        cart_item = Cart.objects.get(account=account, product=product_name)
                        cart_item.delete()
                    except ObjectDoesNotExist:
                        pass
                if 'addProduct' in name:
                    print(name[10:])
                    productName = name[10:]
                    product_name = Products.objects.get(name=productName)
                    try:
                        cart_item = Cart.objects.get(account=account, product=product_name)
                        cart_item.quantity = int(info[name])
                        cart_item.save()
                    except ObjectDoesNotExist:
                        pass
        else:
            return redirect('account')
    return redirect('check_out')