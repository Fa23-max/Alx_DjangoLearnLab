from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.list_books,name="list_books")
    
]