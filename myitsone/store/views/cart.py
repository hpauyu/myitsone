from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.cart import Cart
from account.models.account import Account
from store.models.products import Products
from store.models.category import Category


def cart(request):
    content = dict()
    content['categories'] = Category.objects.all()
    products = list()
    if 'user' in request.session:
        if 'cart' in request.session:
            return redirect('add_cart')
        account = Account.get_account_by_id(request.session['user'])
        cart = Cart.objects.filter(account=account)
        if len(cart) ==0:
            return redirect('account')
        for cart_item in cart:
            product_dict = dict()
            product = cart_item.product
            product_dict['name'] = product.name
            product_dict['price'] = product.sell_price
            product_dict['image'] = product.image.url
            product_dict['quantity'] = cart_item.quantity
            product_dict['total'] = cart_item.quantity * product.sell_price
            products.append(product_dict)
    if 'user' not in request.session:
        if 'cart' not in request.session:
            return redirect('index')
        cart_list = request.session['cart']
        print(request.session['cart'])
        name_list = cart_list.keys()
        for cart_product_name in name_list:
            product_dict = dict()
            product_dict['name'] = cart_product_name
            product = Products.objects.get(name=cart_product_name)
            product_dict['price'] = product.sell_price
            product_dict['image'] = product.image.url
            product_dict['quantity'] = cart_list[cart_product_name]
            product_dict['total'] = cart_list[cart_product_name] * product.sell_price
            products.append(product_dict)
    content['products'] = products
    return render(request,'cart.html',content)