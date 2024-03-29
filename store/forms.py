from django import forms
from .models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class CustomerForm(forms.ModelForm):
#     user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)

#     class Meta:
#         model = Customer
#         fields = ['user', 'name', 'email']

        
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


