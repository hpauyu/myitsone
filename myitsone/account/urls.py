from django.urls import path
from .views.account import account,logout
from .views.login import login
from .views.register import register
from .views.orderdetail import orderdetail
from .views.addorder import add_order



urlpatterns = [
    path('',account,name='account'),
    path('login',login,name='login'),
    path('register',register,name='register'),
    path('logout',logout,name='logout'),
    path('order/<str:str>',orderdetail,name ='orderdetail'),
    path('add-order',add_order,name='add_order')
    #
    # path('order',order,name='order'),
    #
    #
]
