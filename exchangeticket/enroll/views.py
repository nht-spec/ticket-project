from django import forms
from django.shortcuts import render, HttpResponseRedirect
from .forms import TicketRegistration
from .models import User
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_page(request):
    stud = User.objects.all()
    return render(request, 'enroll/homepage.html', {'stu':stud})

@login_required(login_url="/accounts/login/")  
def add_show(request):
    if request.method == 'POST':
     fm = forms.TicketRegistration(request.POST,request.FILES)
     if fm.is_valid():
        nm = fm.cleaned_data['name']
        de = fm.cleaned_data['desc']
        thum = fm.cleaned_data['thumnail']
        qua = fm.cleaned_data['quality']
        pri = fm.cleaned_data['price']
        time = fm.cleaned_data['time_pub']
        reg = User(name=nm, desc=de, thumnail=thum, quality=qua, price=pri,time_pub=time)
        reg.save()
     fm = TicketRegistration()
    else:
     fm = TicketRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 
    'stu':stud})

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = TicketRegistration(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
         fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = TicketRegistration(instance=pi)
    return render(request, 'enroll/updateticket.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
       pi = User.objects.get(pk=id)
       pi.delete()
       return HttpResponseRedirect('/myticket')

def enroll_create(request):
    return render(request,'enroll/enroll_create.html')