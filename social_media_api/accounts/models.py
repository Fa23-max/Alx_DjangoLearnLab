from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='static/img',blank=True, null=True)
    followers = models.ManyToManyField('self',related_name='following',symmetrical=False)

    def __str__(self):
        return self.username

       
   


