from django.db import models
from store.models.products import Products
from account.models.account import Account

class Cart(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name