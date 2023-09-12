from django.db import models
from .account import Account
import uuid
from django.urls import reverse


class UserAddress(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    house_address = models.CharField(max_length=254)
    ward = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    special_instruction = models.CharField(max_length=254, blank=True)
    contactPhone = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.ward
