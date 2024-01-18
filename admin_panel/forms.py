from django import forms
from .models import *

class SignInForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput( attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
