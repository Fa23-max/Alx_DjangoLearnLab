from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.PostViewSet.as_view(),name="post"),
    path('comment/',views.CommentViewSet.as_view(),name="comment"),
    #"feed/"
    #"<int:pk>/like/"
    #"<int:pk>/unlike/"
]
