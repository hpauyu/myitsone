import requests
import os

telegram_token = os.environ.get('TELEGRAM_BOT_TOKEN')
chat_id = os.environ.get('TELEGRAM_CHAT_ID')


def newOrderNoti(order):
    order_id = order.id
    user_address = order.user_address
    amount = order.amount
    user_payment = order.user_payment
    created_date = order.created_date
    send_text = f'https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={str(chat_id)}' \
                f'&text=Order : {order_id}\n' \
                f'Address     : {user_address}\n' \
                f'Amount      : {amount} MMK\n' \
                f'Payment     : {user_payment}\n' \
                f'created_date: {created_date}\n' \
                f'Link        : {order.get_absolute_url}'
    try:
        response = requests.get(send_text)
    except:
        pass
