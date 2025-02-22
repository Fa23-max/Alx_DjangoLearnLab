from django.views.generic.list import DetailView 
from django.shortcuts import render
from .models import Library,Book




# Create your views here.
def list_books(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html",{"books":books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context
    
    




