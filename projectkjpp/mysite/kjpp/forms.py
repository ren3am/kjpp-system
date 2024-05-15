# forms.py

from django import forms
from django.forms import ModelForm
from .models import akun

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
# forms.py

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class MyForm(forms.Form):
    text_field = forms.CharField(max_length=100)

class RegisterForm(ModelForm):
    username = forms.TextInput()
    password = forms.TextInput()
    class Meta:
        model = akun
        fields = ['username', 'password']
