from django.db import models
from django.contrib.auth.models import User,AbstractUser,UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from bookshelf.models import CustomUser



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




