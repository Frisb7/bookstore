from django.db import models
from account.models import Account
from inventory.models import Book, Log
from django.db.models.signals import post_save

# Create your models here.

class Cart(models.Model) :
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_type = models.CharField(max_length=100, editable=False)
    quantity = models.IntegerField(default=1)
    cost = models.DecimalField(max_digits=5, decimal_places=3, editable=False)
    total_cost = models.DecimalField(max_digits=7, decimal_places=3, editable=False)

    def __str__(self) :
        return(("{}: {}").format(self.user, self.book_name))
    
    def save(self, *args, **kwargs) :
        book = Book.objects.get(name=self.book_name)
        self.book_type = book.book_type
        self.cost = book.cost
        self.total_cost = self.quantity * self.cost
        super(Cart, self).save(*args, **kwargs)