from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import post , Comment
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ('title', 'tags',)
        widgets = {
            'tags': TagWidget(),
        }

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ("username","email")

# class CreatePost(forms.ModelForm):
#     title = forms.CharField()
#     content = forms.CharField()

#     class Meta:
#         model = post
#         fields = ("title","content")

   
class CommentForm(forms.ModelForm):
    content = forms.CharField()

    class Meta:
        model = Comment
        fields = ("content",)




    
    

