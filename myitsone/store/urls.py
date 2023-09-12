from django.urls import path
from .views.index import index
from .views.addcart import addCart
from .views.cart import cart
from .views.editCart import editCart
from .views.checkOut import checkOut
from .views.product import product
from .views.category import category
from .views.search import search


urlpatterns = [
    path('',index,name='index'),
    path('add-cart',addCart,name='add_cart'),
    path('cart',cart,name='cart'),
    path('edit-cart',editCart,name='edit_cart'),
    path('check-out',checkOut,name ='check_out'),
    path('product/<slug:slug>',product,name='product'),
    path('category/<slug:slug>',category, name ='category'),
    path('search',search,name='search'),
]