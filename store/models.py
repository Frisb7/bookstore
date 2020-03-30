from django.db import models
from account.models import Account
from inventory.models import Book
from django.db.models.signals import post_save

# Create your models here.

# class Cart(models.Model) :
#     type_choice = (('Text book', 'Text book'),
#                     ('Long note', 'Long note'),
#                     ('Short note', 'Short note'),
#                     ('Lab record', 'Lab Record'),
#                     ('Graph book', 'Graph book'))
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
#     book_type = models.CharField(max_length=100, choices=type_choice)
#     quantity = models.IntegerField()
#     cost = models.DecimalField(max_digits=10, decimal_places=3)
#     total_cost = models.DecimalField(max_digits=10, decimal_places=3)

#     def __str__(self):
#         return(("{}: {}").format(self.user, self.book_name))