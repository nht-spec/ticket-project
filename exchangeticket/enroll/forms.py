
from django.core import validators
from django import forms
from django.db import models
from .models import Ticket,TicketReview


class TicketRegistration(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['name','desc','category','thumnail','quality','price','time_pub']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'quality': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'time_pub': forms.DateTimeInput(attrs={'class':'form-control'}),
        }

class ReviewAdd(forms.ModelForm):
    	class Meta:
            model=TicketReview
            fields=('review_text','review_rating')
