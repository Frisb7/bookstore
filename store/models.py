from django.db import models

# Create your models here.
# class User(models.Model) :
#     grade_choice = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10','10'), ('11','11'), ('12','12'))
#     grno = models.IntegerField()
#     fname = models.CharField(max_length=100)
#     lname = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     garde = models.CharField(max_length=100, choices=grade_choice)

#     def __str__(self):
#         return(self.fname)

class Cart(models.Model) :
    type_choice = (('Text book', 'Text book'),
                    ('Long note', 'Long note'),
                    ('Short note', 'Short note'),
                    ('Lab record', 'Lab Record'),
                    ('Graph book', 'Graph book'))
    user = ForeignKey(User, on_delete=models.DO_NOTHING)
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_type = models.CharField(max_length=100, choices=type_choice)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    total_cost = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return(("{} {}").format(self.user, self.book_name))