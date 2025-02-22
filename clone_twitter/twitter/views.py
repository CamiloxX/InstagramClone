from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Post, Relationship
from .forms import UserForm, PostForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse



def custom_logout(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige a la página de login

@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    context = {'posts': posts, 'form' : form}
    return render(request, 'twitter/newsfeed.html', context)  

def register_view(request):
    if request.method == 'POST': 
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()
    context = {'form' : form}
    return render(request, 'twitter/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def editar_view(request):
    return render(request, 'twitter/editar.html')

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    
    if request.user == post.user:
        post.delete()

    return HttpResponseRedirect(reverse('home')) 

def profile(request, username):
    user = User.objects.get(username = username)
    posts = user.posts.all()
    context = {'user':user, 'posts':posts}
    return render(request, 'twitter/profile.html', context)

@login_required
def editar(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm()
    context = {'u_form' : u_form, 'p_form' : p_form}
    return render(request, 'twitter/editar.html', context)

@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('home')

@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.get(from_user=current_user.id, to_user=to_user_id)
    rel.delete()
    return redirect('home')