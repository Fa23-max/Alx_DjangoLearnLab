from django.views.generic.list import ListView
from django.shortcuts import render
from .models import Book,Library




# Create your views here.
def list_books(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html",{"books":books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context
    
    




