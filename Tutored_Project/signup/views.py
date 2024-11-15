from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, SignInForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.contrib import messages
from django.template.loader import get_template
from django.template import context
from django.contrib.auth import login






# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"AccountCreated!")
            return redirect('index')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})    

def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())
def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username=request.POST['username'],
            password=request.POST['password'],
            user = authenticate(username=username, password=password)

           

            if user is not None:
                login(request, user)
                return redirect('index.html')
        else:
            messages.error(request,"Error!") 
    else:
        form = SignInForm() 
    
                
                
            
    return render(request, 'signin.html', {'form': form})    
