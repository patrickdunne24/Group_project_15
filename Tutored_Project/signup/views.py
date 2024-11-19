from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, SignInForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from .tokens import account_activation_token
from django.contrib import messages
from django.template.loader import get_template, render_to_string
from django.template import context
from django.contrib.auth import login
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage





def verify_email(request):
    if request.method == "POST":
        currentSite = get_current_site(request)
        user = request.user
        email = request.user.email
        subject = "Verify Email"
        message = render_to_string("'verify_email_message", {
            'request': request,
            'user': user,
            'domain': currentSite.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        email = EmailMessage(
            subject, message, to=[email]
        )
        email.content_subtype ='html'
        email.send()
        return (redirect('verify_email_done'))
    
    return render(request, 'verify_email.html')    



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
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT user_id, username, _password FROM dbo.users WHERE username = %s", [username])
                data = cursor.fetchone()
                if data:
                    user_id, db_username, db_password = data
                    if password == db_password:
                        if username == db_username:
                            user = authenticate(db_username, db_password)
                            
                            login(request, user)
                            return(redirect, 'index')
                        else:
                            messages.error(request, "Wrong details")
                    else:
                       messages.error(request, "Wrong details")
                    
                else:
                    messages.error(request, "User not found")
            except Exception as e: 
                messages.error(request, f"Error occured {e}")
        else:
            messages.error(request, "Invalid Form")        
    else:
        form = SignInForm() 
    return render(request, 'signin.html', {'form': form})    


