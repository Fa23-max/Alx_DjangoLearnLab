from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):  
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='static/img/', blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
    

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
    
 
class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ManyToManyField(Post)
