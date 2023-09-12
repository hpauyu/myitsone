from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models.cart import Cart
from account.models.account import Account
from account.models.useraddress import UserAddress
from store.models.products import Products
from forms import UserAddress as UserAddressForm
from store.models.category import Category




def checkOut(request):
    if 'user' not in request.session:
        return  redirect('account')
    account = Account.get_account_by_id(request.session['user'])
    content = dict()
    content['categories'] = Category.objects.all()
    products = list()
    cart = Cart.objects.filter(account=account)
    if len(cart) == 0:
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
    content['products'] =products
    initial = dict()
    try:
        address = UserAddress.objects.filter(account= account).last()
        initial['house_address'] = address.house_address
        initial['ward'] = address.ward
        initial['special_instruction'] = address.special_instruction
        initial['contactPhone'] = address.contactPhone
        initial['city'] = address.city
    except :
        pass
    user_address_form = UserAddressForm(initial=initial)
    content['user_address_form'] = user_address_form

    return render(request,'checkout.html',content)