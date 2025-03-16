from .models import Book ,Author
from .serializers import BookSerializer ,AuthorSerializer
from rest_framework import generics , filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework ,DjangoFilterBackend


class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    ordering_fields =['title','publiation_year']
    search_fields = ['title','author_author_name']
    filterset_fields = ['title','author','publication_year']

class DetailViews(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView ):
   # permission_classes = (IsAuthenticatedOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView ):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

