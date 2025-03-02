from django.db import models
from django.contrib.auth.models import User,AbstractUser,UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
   date_of_birth = models.DateField()
   profile_photo = models.ImageField()

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    class Meta(models.Model):
        permissions = (('can_add_book','can_add_book'),('can_change_book','can_change_book'),('can_delete_book','can_delete_book'))
        

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
  name = models.CharField(max_length=100)
  library = models.OneToOneField(Library,on_delete=models.CASCADE,related_name='librarian')
    



class UserProfile(models.Model):
  user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
  role = models.CharField(choices=(('Admin','Admin'),('Librarian','Librarian'),('Member','Member')), max_length=50)
  UserProfile = models.TextField()

  def _str_(self):
      return self.user.username
  
  @receiver(post_save, sender=CustomUser)
  def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

  @receiver(post_save, sender=CustomUser)
  def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()




class CustomUserManager(UserManager):
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