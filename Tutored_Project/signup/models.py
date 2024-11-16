
# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    pass 
    name = models.CharField(("name"), max_length=50)