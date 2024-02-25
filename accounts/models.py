from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, Lastname, username, email, password=None):
        if not email:
            raise ValueError('User must have an emmail address!')
        if not username:
            raise ValueError('user must have an username!')

        user = self.model(
            email=self.normalize_email(email), # normalize_email if you enter a capital letter it will insert small letter 
            username = username,
            first_name = first_name,
            Lastname = Lastname
        )#this is creating normal user

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, Lastname, email, username, password):
        
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            Lastname = Lastname
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user #this will creating a super user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    Lastname   = models.CharField(max_length=50)
    username  = models.CharField(max_length=50, unique=True)
    email     = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True) 
    last_login  = models.DateTimeField(auto_now_add=True)
    is_admin    = models.BooleanField(default=False)
    is_staff    = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email' #this will serve as login email address
    REQUIRED_FIELDS = ['username', 'first_name', 'Lastname']  # this will require  

    objects = MyAccountManager()

    def _str_(self):
        return self.email #this will written as email address in django
    
    def has_perm(self, perm, obj=None): # user is_admin has a permission
        return self.is_admin # to do changes of this
    
    def has_module_perms(self, add_label):
        return True  #always return true
