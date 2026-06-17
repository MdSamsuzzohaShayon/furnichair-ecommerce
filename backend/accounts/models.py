from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser

"""
Using a custom user model when starting a project -> https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
A full example -> https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example
Custom users and django.contrib.admin-> https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#custom-users-and-django-contrib-admin
Overriding predefined model methods -> https://docs.djangoproject.com/en/4.2/topics/db/models/#overriding-predefined-model-methods
"""



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("User must have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have `is_staff=True`')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have `is_superuser=True`')
        
        return self.create_user(email, password, **extra_fields)
        # user.is_admin = True
        # user.save(using=self._db)
        # return user
    


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=40, unique=True)
    is_validated = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects  = UserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class Address(models.Model):
    user = models.ForeignKey(User, related_name="address", on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="Bangladesh", blank=True, null=True)
    phone = models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=255)

    def __str__(self)-> str:
        return self.area
    
