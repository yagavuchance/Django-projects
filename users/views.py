from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def register(request):
   if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           login(request,form.save())
           return redirect("users:login")
   else:
       form = UserCreationForm()
   return render(request,'register.html', {'form': form})

def login_user(request):
    if request.method =="POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
               return redirect("manunited:players")
        
    else:
        form = AuthenticationForm()
    return render(request,'login.html', {'form': form})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("manunited:players")



