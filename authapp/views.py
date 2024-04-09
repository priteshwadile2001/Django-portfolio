from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        get_email = request.POST.get('email')
        get_password = request.POST.get('password1')
        get_confirm_password = request.POST.get('password2')
        if get_password != get_confirm_password:
            messages.info(request, 'Passwords do not match!')
            return redirect("/auth/signup/")
        
        try:
            User.objects.get(username=get_email)
            messages.info(request, 'Email is already taken!')
            return redirect("/auth/signup/") 
        except User.DoesNotExist:
            pass
        
        myuser = User.objects.create_user(get_email, get_email, get_password) #username , email , password
        myuser.save()
        messages.success(request, 'User is created, please login.')
        return redirect("/auth/login/")

    return render(request, 'signup.html')

def handleLogin(request):
    if request.method=="POST":
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        myuser= authenticate(username=get_email,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request,'login.html')

