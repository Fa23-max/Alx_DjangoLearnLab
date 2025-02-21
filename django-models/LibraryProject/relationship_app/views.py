from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Book,Library




# Create your views here.
def list_books(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html",{"books":books})







