from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view() ,name ="logout"),
    path('',views.index, name="home"),
    path('profile/',views.profile, name="profile"),
    path('posts/',views.Display_blog.as_view(), name= "Display_blog"),
    path('posts/<int:pk>',views.Blog_details.as_view(),name="Blog_details"),
    path('post/new/',views.Create_blog.as_view(),name="Create_blog"),
    path('post/<int:pk>/update/',views.Update_blog.as_view(),name="Update_blog"),
    path('post/<int:pk>/delete/',views.Delete_blog.as_view(),name="Delete_blog"),



]



 