from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse,reverse_lazy
from .forms import RegistrationForm
from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView
from .models import post
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


class Display_blog(ListView):
    model = post
    template_name = "blog/post_list.html"
    context_object_name = "blogs"

class Blog_details(DetailView):
    model = post
    template_name ="blog/post_detail.html"
    context_object_name = "blogs"

class Create_blog(LoginRequiredMixin,CreateView):
    model = post
    template_name = "blog/post_form.html"
    fields = ["title","content"]
    success_url =reverse_lazy("Display_blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class Update_blog(LoginRequiredMixin,UpdateView,UserPassesTestMixin):
    model = post
    template_name ="blog/post_form.html"
    fields = ["title","content"]
    success_url = reverse_lazy("Display_blog")

    def test_func(self):
        return self.request.user == self.get_object().author


class Delete_blog(DeleteView):
    model = post
    template_name ="blog/post_delete.html"
    success_url ="/"



    
    

