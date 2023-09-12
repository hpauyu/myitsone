from django.contrib import admin
from .models.products import Products
from .models.inventory import Inventory
from .models.productinfo import ProductInfo
from .models.category import Category
from .models.cart import Cart
from store.models.search import Search


class Populated(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
class ViewProducts(admin.ModelAdmin):
    list_display = ['name','sell_price']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Products,ViewProducts)


class ViewInventory(admin.ModelAdmin):
    list_display = ['product','quantity']


admin.site.register(Inventory,ViewInventory)
admin.site.register(ProductInfo)
admin.site.register(Category,Populated)

class ViewCart(admin.ModelAdmin):
    list_display = ['product','quantity']
admin.site.register(Cart,ViewCart)


class ViewSearch(admin.ModelAdmin):
    list_display = ['name','result']
admin.site.register(Search,ViewSearch)