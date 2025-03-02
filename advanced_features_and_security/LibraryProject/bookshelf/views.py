from django.shortcuts import render,redirect
from .forms import Bookform,Book
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':	
        form = Bookform(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            form.save()
            return redirect('book_list')
    else:
        form = Bookform()
    return render(request, 'bookshelf/edit-book.html', {'form':form})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookshelf/book_list.html', {"books":books})