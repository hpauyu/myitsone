from django.urls import path
from .views.manager import manager
from .views.add_product import add_product
from .views.all_products import all_products
from .views.edit_product import edit_product
from .views.orders import pending_orders,order,confirmed_orders,out_for_delivery_orders,completed_orders


urlpatterns = [
    path('',manager,name='manager'),
    path('add-product',add_product,name='add_product'),
    path('all-products',all_products,name='all_products'),
    path('edit-product/<slug:slug>',edit_product,name='edit_product'),
    path('orders/pending',pending_orders,name='pending-orders',),
    path('orders/confirmed',confirmed_orders,name='confirmed-orders',),
    path('orders/out-for-delivery',out_for_delivery_orders,name='out-for-delivery-orders',),
    path('orders/completed',completed_orders,name='completed-orders',),
    path('order/<str:str>',order,name='order'),

]