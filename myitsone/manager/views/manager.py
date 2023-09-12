from django.shortcuts import render,redirect
from django.http import HttpResponse
from decorators import authenticated_manager
from account.models.orderdetail import OrderDetail




# Create your views here.
@authenticated_manager
def manager(request):
    orders = OrderDetail.objects.filter(order_status ='Pending')
    content = dict()
    content['orders'] = orders

    return render(request,'manager/manager.html',content)