from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView 
from .models import Library,Book
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import user_passes_test, login_required,permission_required




def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("/")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

class CustomLoginView(LoginView):
    template_name = 'Login.html'

class CustomLogoutView(LogoutView):
    template_name = 'Login.html'

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


def check_admin(user):
    return user.userprofile.role == 'Admin'

def check_librarian(user):
    return user.userprofile.role == 'Librarian'

def check_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_admin)
def admin_view(request):
    return render(request,'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_librarian)
def librarian_view(request):
    return render(request,'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_member)
def member_view(request):
    return render(request,'relationship_app/member_view.html')


@permission_required("relationship_app/can_add_book")
def can_add_book_view(request):
    return render(request,"relationship_app/can_add_book.html")

@permission_required("relationship_app/can_change_book")
def can_change_book_view(request):
    return render(request,"relationship_app/can_change_book.html")

@permission_required("relationship_app/can_delete_book")
def can_delete_book_view(request):
    return render(request,"relationship_app/can_delete_book.html")