# UserManagement/views.py
from django.shortcuts import render
from .models import CustomUser

def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'UserManagement/user_list.html', {'users': users})