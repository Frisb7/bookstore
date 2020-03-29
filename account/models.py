from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Manager(BaseUserManager) :
    def create_user(self, email, username, first_name, last_name, grno, password=None) :
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
        
        user = self.models(email = self.normalize_email(email),
                            username = username,
                            )
        user.set_password(password)
        user.save(using=slef._db)
        return(user)

    def create_superuser(self, email, username, first_name, last_name, grno, password=None) :
        user = self.create_user(email = self.normalize_email(email),
                            username = username,
                            password=password,
                            first_name=first_name,
                            last_name=last_name,
                            grno=grno,
                            )
        is_admin = True
        is_staff = True
        is_superuser = True
        user.save(using=slef._db)
        return(user)

class Accounts(AbstractBaseUser):
    email                       = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username                    = models.CharField(max_length=30, unique=True)
    first_name                  = models.CharField(max_length=30, blank=False)
    last_name                   = models.CharField(max_length=30, blank=True)
    grno                        = models.IntegerField()
    is_admin                    = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    is_staff                    = models.BooleanField(default=False)
    is_superuser                = models.BooleanField(default=False)
    date_joined                 = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','grno',]

    objects = Manager()

    def __str__(self) :
        return(("{}: {}").format(self.first_name, self.email))
    
    def has_perm(self, perm, obj=None) :
        return(self.is_admin)

    def has_module_perm(self, app_label) :
        return(True)
