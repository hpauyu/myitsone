from django.contrib import admin
from.models.account import Account
from .models.orderdetail import OrderDetail
from . models.useraddress import UserAddress
from .models.userpayment import UserPayment
from .models.orderitems import OrderItems


class View(admin.ModelAdmin):
    list_display = ['id','name','username','password','email','password','phone','level','created_date']


class ViewOrderDetail(admin.ModelAdmin):
    list_display = ['id','account','amount','payment_status','order_status']


# Register your models here.
admin.site.register(Account,View)
admin.site.register(OrderDetail,ViewOrderDetail)

class ViewUserAddress(admin.ModelAdmin):
    list_display = ['account','house_address', 'ward','city','contactPhone']


admin.site.register(UserAddress,ViewUserAddress)

class ViewUserPayment(admin.ModelAdmin):
    list_display = ['account','payment_type','payment_provider','account_no']


admin.site.register(UserPayment,ViewUserPayment)

class ViewOrderItems(admin.ModelAdmin):
    list_display = ['account','product','quantity']

admin.site.register(OrderItems,ViewOrderItems)