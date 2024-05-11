from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm
from django.contrib.auth.models import User
class CustomerRegisterForms(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'})) 
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForms(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class PasswordReset(PasswordChangeForm):
    pass

from .models import Customer
class ProfileForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'locality', 'city', 'state', 'mobile', 'zipcode')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }