from django.shortcuts import render,redirect
from django.http import HttpResponse
from account.models.account import Account

def authenticated_manager(view_func):
    def wrapper_func(request,*args,**kwargs):
        if 'user' not in request.session:
            return HttpResponse('log in please')
        else:
            account = Account.get_account_by_id(request.session['user'])
            if account.level == 3:
                return view_func(request, *args, **kwargs)
            elif account.level ==2:
                return HttpResponse('rider')
            else:
                return redirect('account')
    return wrapper_func

def authenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if 'user' not in request.session:
            return redirect('account')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func