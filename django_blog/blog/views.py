from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .forms import RegistrationForm,CommentForm
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView
from .models import Post,Comment 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.decorators import login_required





def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request,"blog/register.html",{"form":form})

def index(request):
    return render (request ,'blog/index.html')

@login_required
def profile(request):
    if request.method == "POST":
        w = request.POST["username"]
        x = request.POST["email"]
        y = request.POST["bio"]
        z = request.POST["profile_img"]
        context = {"username":w,"email":x,"bio":y,"profile_img":z}
        return render(request,'blog/profile.html',context)

    return render(request,'blog/profile.html')

def searchPost(request,pk):
    if request.method == "POST":
        user_search = request.POST["search"]
        title_check = Post.objects.filter(title__icontains = user_search)
        tegs_check = Post.objects.filter(tags__name__icontains = user_search)
        content_check = Post.objects.filter(content__icontains = user_search)

    return HttpResponseRedirect(reverse("home"))  


class Display_blog(ListView):
    model = Post
    template_name = "blog/p_list.html"
    context_object_name = "blogs"


class Blog_details(DetailView):
    model = Post
    template_name ="blog/post_detail.html"
    context_object_name = "blogs"

class Create_blog(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title","content"]
    success_url =reverse_lazy("Display_blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class Update_blog(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model = Post
    template_name ="blog/post_form.html"
    fields = ["title","content"]
    success_url = reverse_lazy("Display_blog")

    def test_func(self):
        return self.request.user == self.get_object().author


class Delete_blog(DeleteView):
    model = Post
    template_name ="blog/post_delete.html"
    success_url ="/"


class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = "blog/comment_form.html"
    form_class = CommentForm
    success_url =reverse_lazy("Display_blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model = Comment
    template_name ="blog/comment_form.html"
    form_class = CommentForm
    success_url = reverse_lazy("Display_blog")

    def test_func(self):
        return self.request.user == self.get_object().author

class CommentDeleteView(LoginRequiredMixin,DeleteView,UserPassesTestMixin):
    model = Post
    template_name ="blog/comment_delete.html"
    success_url ="/"

    def test_func(self):
        return self.request.user == self.get_object().author

class PostByTagListView(ListView):
    model = Post
    def get_queryset(self):
        return super().get_queryset()
    

    

