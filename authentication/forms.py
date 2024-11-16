from .models import CustomUser
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150, widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        widgets = {"password": forms.PasswordInput()}
