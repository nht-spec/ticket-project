from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect, render,redirect
from django.db.models import Avg
from django.http import JsonResponse
from cart.cart import Cart
from django.core.paginator import Paginator
from . import forms
from .forms import TicketRegistration,ReviewAdd
from .models import  Category, Ticket,TicketReview


def home_page(request):
    category = Category.objects.all()
    CATID = request.GET.get('categories')
    stud = Ticket.objects.all()

    if CATID:
        stud = Ticket.objects.filter(category=CATID)
        ticket_paginator = Paginator(stud,12)
        page_num = request.GET.get('page')
        page = ticket_paginator.get_page(page_num)
    else:
        ticket_paginator = Paginator(stud,6)
        page_num = request.GET.get('page')
        page = ticket_paginator.get_page(page_num)
   
    context = {
    'count': ticket_paginator.count,
    'page':page,
    'data':category,
    }
    return render(request, 'enroll/homepage.html',context)

@login_required(login_url="/accounts/login/")  
def add_show(request):
    if request.method == 'POST':
     fm = forms.TicketRegistration(request.POST,request.FILES)
     if fm.is_valid():
        instance = fm.save(commit=False)
        instance.author = request.user
        instance.save()
     fm = TicketRegistration()
    else:
     fm = TicketRegistration()
    stud = Ticket.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 
    'stu':stud})

def update_data(request, id):
    if request.method == 'POST':
        pi = Ticket.objects.get(pk=id)
        fm = TicketRegistration(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
         fm.save()
    else:
        pi = Ticket.objects.get(pk=id)
        fm = TicketRegistration(instance=pi)
    return render(request, 'enroll/updateticket.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
       pi = Ticket.objects.get(pk=id)
       pi.delete()
       return HttpResponseRedirect('/myticket')

def enroll_create(request):
    return render(request,'enroll/enroll_create.html')


@login_required(login_url="/accounts/login/")  
def ticket_detail(request,id):
    stud = Ticket.objects.get(id=id)
    ticket = Ticket.objects.get(id=id)

    
    reviewForm = ReviewAdd()
    
    canAdd=True
    reviewCheck=TicketReview.objects.filter(user=request.user,ticket=ticket).count()
    if request.user.is_authenticated:
        if reviewCheck > 0:
            canAdd=False
	# End
    reviews=TicketReview.objects.filter(ticket=ticket)
    avg_reviews=TicketReview.objects.filter(ticket=ticket).aggregate(avg_rating= Avg('review_rating'))

    return render(request,'enroll/ticket_detail.html', {'data':stud,'form':reviewForm,'canAdd':canAdd,'reviews':reviews,'avg_reviews':avg_reviews})

def search(request):
    q=request.GET['q']
    data = Ticket.objects.filter(name=q,).order_by('-id')
    return render(request,'enroll/search.html',{'data':data})


@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Ticket.objects.get(id=id)
    cart.add(product=product)
    return redirect("homepage")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Ticket.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Ticket.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Ticket.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'enroll/cart_detail.html')


def save_review(request,pid):
    ticket=Ticket.objects.get(pk=pid)
    user= request.user
    review= TicketReview.objects.create(
        user=user,
        ticket=ticket,
        review_text=request.POST['review_text'],
        review_rating=request.POST['review_rating'],
    )
    data={
        'user':user.username,
        'review_text':request.POST['review_text'],
        'review_rating':request.POST['review_rating'],
    }
    return JsonResponse({'bool':True,'data':data})
    
