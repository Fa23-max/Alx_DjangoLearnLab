from rest_framework import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets.ModelViewSet

def BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset
        name_filter = self.request.query_params.get('name', None)
        if name_filter is not None:
            queryset = queryset.filter(name__icontains=name_filter)
        return queryset
    
def BookViewSet(ModelViewSet):
    queryset =Book.objects.all()