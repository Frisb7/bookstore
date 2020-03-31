from django.contrib import admin
from .models import *

# Register your models here.

class BookAdmin(admin.ModelAdmin) :
    field = ('name', 'subject', 'book_type', 'grade', 'stock', 'cost')
    list_display = ('name', 'subject', 'book_type', 'grade', 'stock', 'cost')
    search_fields = ('name', 'subject', 'book_type', 'grade')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class LogAdmin(admin.ModelAdmin) :
    field = ('date', 'user', 'book_name', 'book_type')
    list_display = ('date', 'user', 'book_name', 'book_type')
    search_fields = ('date', 'user', 'book_name', 'book_type')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Book, BookAdmin)
admin.site.register(Log, LogAdmin)