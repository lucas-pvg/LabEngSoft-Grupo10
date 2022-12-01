from django.urls import path, include
from .views import *

urlpatterns = [
   path('register/', UserRegisterView.as_view(), name = 'register'),
]
