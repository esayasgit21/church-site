from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from .forms import RegisterUserForm

def login_user(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
             # Redirect to a success page. 
            return redirect('index')                 
        else:
            messages.success(req, ('Your username and password didn\'t match. Please try again....'))
            return redirect('login')         
    else:
        return render(req,'authenticate/login.html', {})
    
def logout_user(req):
    logout(req)
    messages.success(req,"You Were Successfully Logout...")
    return redirect('index')

def register_user(req):
    try:
        if req.method == 'POST':
            form = RegisterUserForm(req.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username = username, password = password)
                login(req,user)
                messages.success(req,("User Registration Successful!"))
                return redirect('index')
            else:
                messages.error(req,('Please check the error and try again...'))
                return render(req, 'authenticate/register_user.html', {'form': RegisterUserForm()})
        else:
            form = RegisterUserForm()
            return render(req, 'authenticate/register_user.html', {'form': form})
    except:
        messages.error(req,("Unknow error occur plsea contact site admin!"))
        return render(req,'authenticate/register_user.html', {'form': RegisterUserForm()})




    



