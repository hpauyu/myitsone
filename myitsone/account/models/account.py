from django.db import models
from methodsCollection import isValidUsername

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    username = models.CharField(max_length=50,validators=[isValidUsername],null=True,blank=True)
    password = models.CharField(max_length=254,null=True,blank=True)
    email = models.EmailField(max_length=254,null=True,blank=True)
    phone = models.CharField(max_length=30,null=True,blank=True)
    level = models.IntegerField(default=0,null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_account_by_username(username):
        try:
            return Account.objects.get(username=username)
        except:
            return False

    @staticmethod
    def get_level_by_id(id):
        try:
            return Account.objects.get(id = id)
        except:
            return False

    @staticmethod
    def get_account_by_id(id):
        try:
            return Account.objects.get(id=id)
        except:
            return False

    def isPhoneExist(self):
        if Account.objects.filter(phone=self.phone):
            return True
        return False

    def isEmailExist(self):
        if Account.objects.filter(email=self.email):
            return True
        return False

    def isUsernameExist(self):
        if Account.objects.filter(username=self.username):
            return True
        return False


