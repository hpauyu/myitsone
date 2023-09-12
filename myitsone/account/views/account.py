from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models.account import Account
from account.models.orderdetail import OrderDetail
from store.models.category import Category



# Create your views here.
def account(request):
    if 'user' not in request.session:
        return redirect('login')
    account = Account.get_account_by_id(request.session['user'])
    content =dict()
    content['categories'] = Category.objects.all()
    try:
        orders = OrderDetail.objects.filter(account=account).order_by('-created_date')
        content['orders'] = orders
    except:
        pass
    content['account'] = account
    return render(request,'account.html',content)


def logout(request):
    try:
        del request.session['user']
    except KeyError:
        pass
    return redirect('account')


def validateNewUser(account):
    msg=' is already exist'
    if account.isEmailExist():
        return 'Email'+msg
    if account.isPhoneExist():
        return 'Phone'+msg
    if account.isUsernameExist():
        return 'Username'+msg
    return True

