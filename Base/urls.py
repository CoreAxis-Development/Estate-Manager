from django.urls import path
from .views import unauth_error

urlpatterns = [
    path('error/unauth', unauth_error, name='unauth_error'),
   
]