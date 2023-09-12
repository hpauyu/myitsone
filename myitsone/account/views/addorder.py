from django.http import HttpResponse
from django.shortcuts import render,redirect
from forms import UserAddress as UserAddressForm
from account.models.account import Account
from account.models.useraddress import UserAddress
from account.models.userpayment import UserPayment
from account.models.orderdetail import OrderDetail
from account.models.orderitems import OrderItems
from store.models.cart import Cart
from telegram_message import newOrderNoti




def add_order(request):
    if 'user' not in request.session:
        return redirect('account')
    user_address_form = UserAddressForm(request.POST)
    account = Account.get_account_by_id(request.session['user'])
    user_address = UserAddress.objects.filter(account= account)
    user_payment = UserPayment.objects.filter(account=account)
    try:
        user_address_form.is_valid()
        new_user_address = UserAddress(account = account,
                                       house_address=user_address_form.cleaned_data['house_address'],
                                       ward=user_address_form.cleaned_data['ward'],
                                       city=user_address_form.cleaned_data['city'],
                                       special_instruction=user_address_form.cleaned_data['special_instruction'],
                                       contactPhone=user_address_form.cleaned_data['contactPhone'])
        new_user_payment = UserPayment(account=account,
                                       payment_type= user_address_form.cleaned_data['payment'],
                                       payment_provider=user_address_form.cleaned_data['payment'],
                                       account_no = user_address_form.cleaned_data['payment'],)
    except:
        return redirect('check_out')
    current_address = None
    if len(user_address) == 0:
        new_user_address.save()
        current_address = new_user_address
    elif len(user_address) >0:
        same = False
        for address in user_address:
            if address.account == new_user_address.account:
                if address.house_address == new_user_address.house_address:
                    if address.ward == new_user_address.ward:
                        if address.city == new_user_address.city:
                            same = True
                            address.special_instruction = new_user_address.special_instruction
                            address.contactPhone = new_user_address.contactPhone
                            address.save()
                            current_address = address
                            break
        if same is False:
            new_user_address.save()
            current_address = new_user_address
    current_payment = None
    if len(user_payment) == 0:
        new_user_payment.save()
        current_payment = new_user_payment
    elif len(user_payment) >0:
        same = False
        for payment in user_payment:
            if payment.payment_type == new_user_payment.payment_type:
                if payment.payment_provider == new_user_payment.payment_provider:
                    if payment.account_no == new_user_payment.account_no:
                        if payment.account == new_user_payment.account:
                            same = True
                            current_payment = payment
                            break
        if same == False:
            new_user_payment.save()
            current_payment = new_user_payment
    amount = request.POST.get('total',None)
    new_order = OrderDetail(account=account, user_address=current_address, amount=amount, user_payment=current_payment,
                            payment_status='Pending',order_status ='Pending')
    new_order.save()
    cart = Cart.objects.filter(account=account)
    for item in cart:
        amount =item.quantity*item.product.sell_price
        new_order_item = OrderItems(account=account,order=new_order, product=item.product, quantity=item.quantity, amount = amount)
        new_order_item.save()
        item.delete()
    newOrderNoti(new_order)
    return redirect('account')