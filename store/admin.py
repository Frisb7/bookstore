from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Cart

# Register your models here.

class CartAdmin(admin.ModelAdmin) :
    field = ('user', 'book_name', 'book_type', 'quantity', 'cost', 'total_cost')
    list_display = ('user', 'book_name', 'book_type', 'quantity', 'cost', 'total_cost')
    search_fields = ('user', 'book_name', 'book_type')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.site_header = 'Bookstore Admin'
admin.site.unregister(Group)
admin.site.register(Cart, CartAdmin)