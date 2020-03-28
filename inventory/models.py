from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model) :
    subject_choice = (('English', 'English'),
                    ('Math', 'Math'),
                    ('Science', 'Science'),
                    ('Physics', 'Physics'),
                    ('Chemestry', 'Chemestry'),
                    ('Biology', 'Biology'),
                    ('Computer Science', 'Computer Science'),
                    ('Social Studies', 'Social Studies'),
                    ('Hindi', 'Hindi'),
                    ('Arabic', 'Arabic'),
                    )
    type_choice = (('Text book', 'Text book'),
                    ('Long note book', 'Long note book'),
                    ('Short note book', 'Short note book')
                    )
    grade_choice = (('1', '1'),
                    ('2', '2'),
                    ('3', '3'),
                    ('4', '4'),
                    ('5', '5'),
                    ('6', '6'),
                    ('7', '7'),
                    ('8', '8'),
                    ('9', '9'),
                    ('10','10'),
                    ('11','11'),
                    ('12','12'),
                    ('All', 'All')
                    )
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, choices=subject_choice)
    book_type = models.CharField(max_length=100, choices=type_choice)
    garde = models.CharField(max_length=100, choices=grade_choice)
    stock = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    

    def __str__(self):
        return(self.name)

class Log(models.Model) :
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    book_name = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    book_type = models.CharField(max_length=100, editable=False, default='')

    def __str__(self):
        return(("{}: {}").format(self.user, self.book_name))
    
    def save(self, *args, **kwargs) :
        book = Book.objects.filter(name=self.book_name).values('book_type').first()
        self.book_type = book['book_type']
        super(Log, self).save(*args, **kwargs)