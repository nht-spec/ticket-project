
from django.core import validators
from django import forms
from django.db import models
from .models import User

class TicketRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','desc','thumnail','quality','price','time_pub']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'quality': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'time_pub': forms.DateTimeInput(attrs={'class':'form-control'}),
        }