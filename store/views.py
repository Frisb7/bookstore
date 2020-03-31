from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import Book
from .models import Cart
from django.db.models import Sum

# Create your views here.

@login_required(login_url='login')
def store(request) :
    books = Book.objects.all()
    context = {'books':books}
    return(render(request, 'store/store.html', context))

@login_required(login_url='login')
def cart(request) :
    user = request.user
    cart = Cart.objects.filter(user=user)
    if len(cart) != 0 :
        total_cost = cart.aggregate(Sum('total_cost'))
        total_cost = str(total_cost['total_cost__sum'])[:-11]
    else :
        total_cost = 0.000
    print(request.user)
    context = {'cart':cart, 'total_cost':total_cost}
    return(render(request, 'store/cart.html', context))