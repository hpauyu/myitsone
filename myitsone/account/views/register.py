from django.shortcuts import render,redirect
from account.models.account import Account
from forms import RegisterForm
from django.contrib.auth.hashers import make_password
from store.models.category import Category




def register(request):
    content =dict()
    content = dict()
    content['categories'] = Category.objects.all()
    registerErrorMessage=''
    if 'user' in request.session:
        return redirect('account')
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        try:
            registerForm.is_valid()
            username = registerForm.cleaned_data['username']
            name = registerForm.cleaned_data['name']
            password = registerForm.cleaned_data['password']
            email = registerForm.cleaned_data['email']
            phone = registerForm.cleaned_data['phone']
            newUser = Account(username=username, name=name, password=password, email=email, phone=phone)
            if validateNewUser(newUser) is True:
                newUser.password = make_password(newUser.password)
                newUser.save()
                request.session['user'] = newUser.id
                return redirect('account')
            else:
                registerErrorMessage = validateNewUser(newUser)
        except:
            registerErrorMessage = 'Username cannot contain space'

        content = {
                'form': registerForm,
                'message': registerErrorMessage
            }
        return render(request, 'register.html', content)
    else:
        registerForm = RegisterForm()
        content['form'] =registerForm
        return render(request,'register.html',content)


def validateNewUser(account):
    msg=' is already exist'
    if account.isUsernameExist():
        return 'Username'+msg
    if account.isEmailExist():
        return 'Email'+msg
    if account.isPhoneExist():
        return 'Phone'+msg
    return True

