from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Cart, CustomUser, ProductInCart, Seller, SellerAdditional
from django import forms
from django.core.validators import  RegexValidator
from .models import Contact

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','name')


class  CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email','name')

# form using forms.Form
# class ContactUsForm(forms.Form):
#     name = forms.CharField(max_length=255,required=True)
#     email = forms.EmailField(required=True)
#     phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message="The format 99999999 upto 14 digit")  
#     phone = forms.CharField(max_length=255,required=True,validators=[phone_regex])
#     query = forms.CharField(widget=forms.Textarea)

# form using model form

from django.forms import TextInput,EmailInput
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {
            'name',
            'email',
            'phone',
            'query'
        }

        # widgets = {
        #     'name': TextInput(attrs={
        #         'class': "form-control",
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Name'
        #         }),
        #     'email': EmailInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Email'
        #         }),
        #     'phone': TextInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Phone'
        #         }),
        #     'query': TextInput(attrs={
        #         'class': "form-control", 
        #         'style': 'max-width: 300px;',
        #         'placeholder': 'Query'
        #         })
            
        # }

# this forms only works when customer or customuser fro email is not created
class RegistrationFormSeller(UserCreationForm):
    gst = forms.CharField(max_length=10)
    warehouse_location = forms.CharField(max_length=255)
    class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
            'gst',
            'warehouse_location'
        ]

# simple basic form
class RegistrationForm(UserCreationForm):
     class Meta:
        model = Seller
        fields = [
            'email',
            'name',
            'password1',
            'password2',
        ]

# simple model form Seller
class RegistrationFormSeller2(forms.ModelForm):
    class Meta:
        model = SellerAdditional
        fields = [
            'gst',
            'warehouse_location'
        ]

class CartForm(forms.ModelForm):
    class Meta:
        model=ProductInCart
        fields = [
            'quantity'
        ]