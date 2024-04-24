from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'confirm password',
    }))