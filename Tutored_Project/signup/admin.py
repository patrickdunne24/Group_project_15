from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import SignUpForm
# Register your models here.

admin.site.register(CustomUser)
