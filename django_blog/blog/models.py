from django.db import models
from django.contrib.auth.models import User

class post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    
class UserProfile(models.Model):  
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='static/img/', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username