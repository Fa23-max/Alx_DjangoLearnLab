from django import forms
from .models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        field = ['title', 'author', 'publication_date']
        
class ExampleForm(forms.Form):
    name =forms.CharField( max_length=100 )
    email = forms.EmailField()

    
   