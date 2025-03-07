from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter ,include
from .views import BookViewSet


router =DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),
]








