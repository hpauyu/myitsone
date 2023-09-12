from django.http import HttpResponse
from django.shortcuts import render,redirect
from account.models.orderdetail import OrderDetail
from account.models.account import Account
from account.models.orderitems import OrderItems
from store.models.category import Category


def orderdetail(request,str):
    if 'user' not in request.session:
        return redirect('login')
    account = Account.get_account_by_id(request.session['user'])
    order = OrderDetail.objects.get(order_id = str,account=account)
    content = dict()
    content['categories'] = Category.objects.all()
    products = OrderItems.objects.filter(order = order,account=account)
    content['products'] = products
    content['order'] = order
    return render(request,'orderdetail.html',content)