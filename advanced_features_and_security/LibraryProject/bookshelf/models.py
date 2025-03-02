from django.db import models
from django.contrib.auth.models import User,AbstractUser,BaseUserManager

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)
  publication_year = models.IntegerField()

class CustomUser(AbstractUser):
   date_of_birth = models.DateField()
   profile_photo = models.ImageField()

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, date_of_birth=None,profile_photo=None,**extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password,date_of_birth, profile_photo,**extra_fields)

    def create_superuser(self, username, email=None, password=None,date_of_birth=None,profile_photo=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(username, email, password,date_of_birth, profile_photo, **extra_fields)