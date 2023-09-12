from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.cart import Cart
from account.models.account import Account
from store.models.products import Products
from django.core.exceptions import ObjectDoesNotExist


def addCart(request):
    if request.method =='GET':
        if len(request.GET) == 0:
            if 'user' in request.session:
                account = Account.get_account_by_id(request.session['user'])
                cart_products = dict()
                if 'cart' in request.session:
                    cart_products = request.session['cart']
                    del request.session['cart']
                save_cart(account=account, cart_products=cart_products)
            return redirect('cart')
        products = request.GET
        data = dict()
        for key in products:
            data[key] = int(products[key])
        products = data
        if 'user' not in request.session:
            if 'cart' in request.session:
                cart=cart_in_session(products,request.session['cart'])
                request.session['cart'] = cart
            else:
                request.session['cart'] = products
        else:
            account = Account.get_account_by_id(request.session['user'])
            cart_products = dict()
            if 'cart' in request.session:
                cart_products = cart_in_session(products,request.session['cart'])
                del request.session['cart']
            else:
                cart_products = products
            save_cart(account=account,cart_products=cart_products)
    return redirect('cart')


def cart_in_session(products,session):
    for key, value in products.items():
        if key in session:
            session[key] += value
        else:
            session[key] = value
    return session


def save_cart(account,cart_products):
    for x in cart_products:
        quantity = cart_products[x]
        product = Products.objects.get(name=x)
        try:
            cart = Cart.objects.get(account=account, product=product)
            cart.quantity += quantity
            cart.save()
        except ObjectDoesNotExist:
            cart_item = Cart(account=account, product=product, quantity=quantity)
            cart_item.save()