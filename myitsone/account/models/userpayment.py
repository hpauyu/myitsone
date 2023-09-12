from django.db import models
from account.models.account import Account

class UserPayment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_type= models.CharField(max_length=254)
    payment_provider = models.CharField(max_length=254)
    account_no = models.CharField(max_length=254)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_type
