from django.db import models
from account.models.orderdetail import OrderDetail
from store.models.products import Products
from account.models.account import Account

class OrderItems(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE ,null=True)
    order = models.ForeignKey(OrderDetail,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
