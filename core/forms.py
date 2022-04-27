from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Item



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

 


class SignUpForm2(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    shop_name = forms.CharField(max_length=100, required=True ,)
    location = forms.CharField(help_text='Your Location')

    class Meta:
        model = User
        fields = ('username', 'shop_name', 'location', 'password1', 'password2',)



from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'PayPal')
)


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)

    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)

    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class EditForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'price',  'category', 'label', 'slug', 'description', 'image')