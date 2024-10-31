# UserManagement/urls.py
from django.urls import path
from .views import user_list_view

urlpatterns = [
    path('users/', user_list_view, name='user_list_view'),
]