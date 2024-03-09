from django.urls import path
from .views import *
urlpatterns = [
    path('register/', register,name='register'),
    path('me/', current_user,name='me'),
    path('me/update/', update_user,name='update-user'),
    path('forget_password/', forgot_password,name='forget-password'),
    path('reset_password/<str:token>', reset_password, name="reset_password"),
    
]
