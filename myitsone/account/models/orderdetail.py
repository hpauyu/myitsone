from django.db import models
from .account import Account
from .useraddress import UserAddress
from .userpayment import UserPayment
import uuid
from django.urls import reverse


class OrderDetail(models.Model):
    ORDER_STATUS =(
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Completed', 'Completed'),
    )
    PAYMENT_STATUS =(
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    order_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    user_address = models.ForeignKey(UserAddress,on_delete=models.CASCADE, null=True)
    amount = models.IntegerField()
    user_payment = models.ForeignKey(UserPayment,on_delete=models.CASCADE, null=True)
    payment_status = models.CharField(max_length=254,null=True,choices=PAYMENT_STATUS)
    order_status = models.CharField(max_length=254,null=True,choices=ORDER_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(null=True,blank=True,max_length=254)

    def get_absolute_url(self):
        return reverse('orderdetail',kwargs={'str':self.order_id})

    def get_absolute_url_manager(self):
        return reverse('order', kwargs={'str': self.order_id})