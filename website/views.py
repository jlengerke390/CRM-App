from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    #Check to see if loggin in
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        #authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           messages.success(request, ("You are now logged in"))
           return redirect('home')
        else:
           messages.error(request, ("Invalid username or password"))
           return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))
    return redirect('home')
    

