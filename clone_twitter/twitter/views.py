from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Profile, Post

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'twitter/newsfeed.html', context)  

def logout_view(request):
    logout(request)
    return redirect('home')

def editar_view(request):
    # Add your view logic here
    return render(request, 'twitter/editar.html')