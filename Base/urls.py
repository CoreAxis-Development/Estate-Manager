from django.urls import path
from .views import unauth_error , home_page

urlpatterns = [
    path('home/', home_page, name='home_page'),
    path('error/unauth', unauth_error, name='unauth_error'),
   
]