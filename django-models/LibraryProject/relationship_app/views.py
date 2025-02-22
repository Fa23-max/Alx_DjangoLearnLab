from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView 
from .models import Library,Book
from django.contrib.auth import login




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def list_books(request):
    books = Book.objects.all()

    return render(request,"list_books.html",{"books":books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context