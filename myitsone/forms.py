from django import forms
from methodsCollection import isValidUsername
from store.models.category import Category


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, validators=[isValidUsername], label='Username', )
    name = forms.CharField(max_length=100, label='Name')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    email = forms.EmailField(max_length=254, required=False)
    phone = forms.CharField(max_length=15, initial='09')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, validators=[isValidUsername], label='Username', )
    password = forms.CharField(widget=forms.PasswordInput, label='Password')


class UserAddress(forms.Form):
    house_address = forms.CharField(max_length=254)
    ward = forms.CharField(max_length=254)
    city = forms.CharField(max_length=254, label='မြို့')
    special_instruction = forms.CharField(max_length=254, widget=forms.Textarea(
        attrs={"rows": "5", 'placeholder': 'What time to send and when arrive home call me'}), required=False)
    contactPhone = forms.CharField(max_length=30, required=True)
    CHOICES = [
        ('Cash on Delivery', 'Cash on Delivery'),
        ('KBZ Pay', 'KBZ Pay'),
    ]
    payment = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
    )


class Product(forms.Form):
    name = forms.CharField()
    original_price = forms.IntegerField()
    sell_price = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select a category", )
    image = forms.ImageField()
    sku = forms.CharField(required=False)
    note = forms.CharField(max_length=254,
                           widget=forms.Textarea(attrs={"rows": "5", 'placeholder': 'What time to send and'
                                                                                    ' when arrive home call me'}),
                           required=False)
    quantity =forms.IntegerField()
