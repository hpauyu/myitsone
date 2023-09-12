from django.shortcuts import render,redirect
from django.http import HttpResponse
from forms import LoginForm
from account.models.account import Account
from django.contrib.auth.hashers import check_password
from store.models.category import Category


def login(request):
    content = dict()
    content['categories'] = Category.objects.all()
    message=''
    if 'user' in request.session:
        return redirect('account')
    if request.method =='GET':
        form = LoginForm()
        content['form'] =form
        return render(request,'login.html',content)
    else:
        loginForm = LoginForm(request.POST)
        try:
            loginForm.is_valid()
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            loginUser = Account.get_account_by_username(username)
            if loginUser:
                if check_password(password,loginUser.password):
                    request.session['user'] = loginUser.id
                    return redirect('account')
                else:
                    message = 'Password Incorrect'
            else:
                message ='Register Now'
        except:
            message = 'Username cannot contain space'
        content= {'form': loginForm,
                  'message' : message}
        return render(request,'login.html',content)
