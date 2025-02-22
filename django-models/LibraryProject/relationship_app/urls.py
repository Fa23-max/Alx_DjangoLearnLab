from . import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books,LibraryDetailView


urlpatterns = [
    path('library_details/',LibraryDetailView.as_view(),name='library_details'),
    path("register/", views.register, name="register"),
    path("",views.list_books,name="list_books"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('admin_view',views.admin_view,name="admin_view"),
    path('librarian_view',views.librarian_view,name="librarian_view"),
    path('member_view',views.member_view,name="member_view"),


]