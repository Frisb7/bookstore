from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from inventory.models import Book
from .models import Cart
from django.db.models import Sum

# Create your views here.

@login_required(login_url='login')
def store(request) :
    books = Book.objects.all().values()
    cart = Cart.objects.filter(user=request.user).values('book_name_id')
    in_cart = []
    for i in cart :
        for j in books :
            if i['book_name_id'] == j['id'] :
                in_cart.append(j)
    context = {'books':books, 'in_cart':in_cart}
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

@login_required(login_url='login')
def add_to_cart(request, pk) :
    book = Book.objects.get(id=pk)
    cart = Cart.objects.create(user = request.user, book_name=book)
    cart.save()
    return(redirect('store'))

@login_required(login_url='login')
def remove_from_cart(request, pk) :
    cart = Cart.objects.get(book_name_id=pk, user=request.user)
    cart.delete()
    return(redirect('store'))