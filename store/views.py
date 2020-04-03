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
    costs = Cart.objects.filter(user=user).values('total_cost')
    sub_total = 0.000
    if len(cart) != 0 :
        for cost in costs :
            sub_total += float(cost['total_cost'])
    else :
        sub_total = 0.000
    sub_total = ('{:.3f}'.format(sub_total))
    context = {'cart':cart, 'sub_total':sub_total}
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

@login_required(login_url='login')
def remove_from_cart2(request, pk) :
    cart = Cart.objects.get(id=pk, user=request.user)
    cart.delete()
    return(redirect('cart'))

@login_required(login_url='login')
def receipt(request) :
    user = request.user
    cart = Cart.objects.filter(user=user)
    costs = Cart.objects.filter(user=user).values('total_cost')
    sub_total = 0.000
    if len(cart) != 0 :
        for cost in costs :
            sub_total += float(cost['total_cost'])
    else :
        sub_total = 0.000
    sub_total = ('{:.3f}'.format(sub_total))
    context = {'cart':cart, 'sub_total':sub_total}
    return(render(request, 'store/receipt.html', context))