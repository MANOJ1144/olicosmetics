from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
import store

def register(request):
    print(request.method)
    if request.method =='POST':
        User.objects.create_user(
            first_name=request.POST['firstname'],
            last_name=request.POST['lastname'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
   
        )
        return redirect('login')
        
    else:
        return render(request, 'store/register.html')

def login(request):
    if request.method == 'POST':
   
        user=authenticate(request, 
        username =request.POST['username'],
        password =request.POST['password'],
        )
        if user is not None:
            auth_login(request, user)
            return redirect('store')
        else:
            return redirect('login')
        
    else:
        return render(request, 'store/login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login')