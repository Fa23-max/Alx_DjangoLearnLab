from django.urls import path
from .views import ListView, DetailViews,CreateView,UpdateView,DeleteView


urlpatterns = [
    path('books/',ListView.as_view(), name = "ListBooks"),
    path('books/<int:pk>',DetailViews.as_view(), name="DetailBooks"),
    path('books/create' ,CreateView.as_view(), name= "Createbooks"),
    path('books/update/<int:pk>' ,UpdateView.as_view(), name="Updatebooks"),
    path('books/delete/<int:pk>' ,DeleteView.as_view(), name="Deletebooks"),



]
