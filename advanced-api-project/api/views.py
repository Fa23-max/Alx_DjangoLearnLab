from .models import Book ,Author
from .serializers import BookSerializer ,AuthorSerializer
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticatedOrReadOnly , IsAuthenticated



class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailViews(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView ):

    permission_classes = (IsAuthenticatedOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

