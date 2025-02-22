from . import views
from django.urls import path,include
from .views import SingUpView,list_books ,LibraryDetailView,TemplateView,LoginView ,LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('library_details/',LibraryDetailView.as_views(),name='library_details'),
    path("register",SingUpView.as_view(),name="templates/registration/register"),
    path("",views.list_books,name="list_books"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/',
             TemplateView.as_view(template_name='accounts/profile.html'),
             name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',LogoutView.as_View(), name='logout')
    
    
]