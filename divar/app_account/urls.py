from django.urls import path
from .views import login_user,register,chat,login_phone


urlpatterns = [
    path('login', login_user),
    path('register', register),
    path('chat', chat),
   path('login_phone',login_phone), 
    
    
]