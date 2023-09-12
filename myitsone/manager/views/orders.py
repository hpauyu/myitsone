from django.shortcuts import render,redirect
from django.http import HttpResponse
from decorators import authenticated_manager
from forms import Product
from store.models.products import Products
from store.models.inventory import Inventory
from account.models.orderitems import OrderItems
from account.models.orderdetail import OrderDetail


@authenticated_manager
def pending_orders(request):
    content=dict()
    orders = OrderDetail.objects.filter(order_status='Pending').order_by('-created_date')
    content['orders'] = orders
    content['header'] = 'Pending'
    return render(request,'manager/orders.html',content)


@authenticated_manager
def confirmed_orders(request):
    content=dict()
    orders = OrderDetail.objects.filter(order_status='Confirmed').order_by('-created_date')
    content['orders'] = orders
    content['header'] = 'Confirmed'
    return render(request,'manager/orders.html',content)


@authenticated_manager
def completed_orders(request):
    content=dict()
    orders = OrderDetail.objects.filter(order_status='Completed').order_by('-created_date')
    content['orders'] = orders
    content['header'] = 'Completed'
    return render(request,'manager/orders.html',content)


@authenticated_manager
def out_for_delivery_orders(request):
    content=dict()
    orders = OrderDetail.objects.filter(order_status='Out for Delivery').order_by('-created_date')
    content['orders'] = orders
    content['header'] = 'Out for Delivery'
    return render(request,'manager/orders.html',content)




@authenticated_manager
def order(request,str):
    content = dict()
    order = OrderDetail.objects.get(order_id=str)
    products = OrderItems.objects.filter(order=order)
    content['order'] =order
    content['products'] = products
    if request.method == 'POST':
        order_status = request.POST['order-status']
        order.order_status = order_status
        order.save()
        return redirect('manager')
    return render(request,'manager/order_detail.html',content)