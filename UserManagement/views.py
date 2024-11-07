# UserManagement/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.middleware.csrf import get_token
from django.views.decorators.csrf import ensure_csrf_cookie
from .forms import UserRegistrationForm
from .models import CustomUser

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            messages.success(request, f'Welcome back, {username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    # Ensure CSRF token is set
    get_token(request)
    return render(request, 'UserManagement/login.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required
def user_list_view(request):
    users = CustomUser.objects.all()
    return render(request, 'UserManagement/user_list.html', {'users': users})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'UserManagement/register.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'UserManagement/home.html', {
        'user': request.user,
    })