from . import views
from django.urls import path,include
from .views import list_books ,LibraryDetailView

urlpatterns = [
    path("",views.list_books,name="list_books")
    
]