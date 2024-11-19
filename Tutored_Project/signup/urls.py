from django.urls import path
from . import views 

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('courses/', views.courses, name='courses'),
    path('signin/', views.signin, name='signin'),
    

    
]