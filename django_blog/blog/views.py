from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('login'))
    return render(request,"registration/register.html",{"form":form})

def index(request):
    return render (request ,'blog/index.html')

def profile(request):
    if request.method == "POST":
        w = request.POST["username"]
        x = request.POST["email"]
        y = request.POST["bio"]
        z = request.POST["profile_img"]
        context = {"username":w,"email":x,"bio":y,"profile_img":z}
        return render(request,'blog/profile.html',context)

    return render(request,'blog/profile.html')


