from django.shortcuts import render,redirect
from .models import Manunited
from django.http import HttpResponseForbidden
from . import forms
from django.contrib.auth.decorators import login_required

def post(request):
    players = Manunited.objects.all()
    return render(request, 'post-player.html', {'players': players})

def details(request, id):
    details = Manunited.objects.get(id=id)
    return render(request, 'details.html', {'details': details})

@login_required(login_url='/users/login/')
def post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost =form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return  redirect("manunited:players")   
    else:
      form = forms.CreatePost()
    
    return render(request, 'new-post.html',{'form': form})

@login_required(login_url='/users/login/')
def edit_post(request, id):
    form = Manunited.objects.get(pk=id)
    if form.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.") 
    if request.method =="POST":
        form = forms.CreatePost(request.POST, instance=form)
        if form.is_valid():
            form.save()
            return redirect("manunited:details", id=id)
    else:
        form =forms.CreatePost(instance=form)
    return render(request,'edit.html',{'form': form})


def delete(request, id):
    form = Manunited.objects.get(pk=id)
    if form.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.") 
    if request.method =="POST":
     form.delete()
     return redirect("manunited:players")
         
        
            
    

