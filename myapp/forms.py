from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


class signuppage(UserCreationForm):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    


    class meta:
        model=User


class loginpage(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
