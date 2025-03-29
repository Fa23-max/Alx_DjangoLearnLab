from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterUserView.as_view(),name="register"),
    path('login/',views.LoginUserView.as_view(),name="login"),
    path('profile',views.RetrieveUserView.as_view(),name="profile"),
    # path('unfollow/<int:user_id>/')
    # path(follow/<int:user_id>)

]
