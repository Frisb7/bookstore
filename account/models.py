from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Manager(BaseUserManager) :
    def create_user(self, email, username, first_name, last_name, grno, garde, password=None) :
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")
        if not first_name:
            raise ValueError("User must have an first name")
        if not last_name:
            raise ValueError("User must have an last name")
        if not grno:
            raise ValueError("User must have an grno")
        if not garde:
            raise ValueError("User must have an garde")
        
        user = self.model(email = self.normalize_email(email),
                            username = username,
                            )
        user.set_password(password)
        user.save(using=self._db)
        return(user)

    def create_superuser(self, email, username, first_name, last_name, grno, password) :
        user = self.create_user(email = self.normalize_email(email),
                            username = username,
                            password=password,
                            first_name=first_name,
                            last_name=last_name,
                            grno=grno,
                            garde=garde,
                            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return(user)

class Account(AbstractBaseUser):
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
                    )
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    grno = models.IntegerField(null=False, blank=False)
    garde = models.CharField(max_length=100, choices=grade_choice)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name','grno', 'garde',]

    objects = Manager()

    def __str__(self) :
        return(("{}: {}").format(self.first_name, self.email))
    
    def has_perm(self, perm, obj=None) :
        return(self.is_admin)

    def has_module_perms(self, app_label) :
        return(True)