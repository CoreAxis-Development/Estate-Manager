# UserManagement/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django_otp import user_has_device, devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice
from .forms import UserRegistrationForm, OTPVerificationForm
from .models import CustomUser
import random

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate a random 6-digit OTP code
            otp_code = str(random.randint(100000, 999999))

            # Send the OTP code to the user's email
            send_mail(
                'Your 2FA OTP Code',
                f'Your one-time password (OTP) is: {otp_code}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            # Store the OTP code and user ID in the session
            request.session['otp_code'] = otp_code
            request.session['user_id'] = user.id

            # Redirect the user to the 2FA verification page
            return redirect('two_factor_authenticate')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'UserManagement/login.html')


def two_factor_authenticate(request):
    user_id = request.session.get('user_id')
    otp_code = request.session.get('otp_code')

    if request.method == 'POST':
        entered_otp = request.POST.get('otp_code')
        if entered_otp == otp_code:
            user = CustomUser.objects.get(id=user_id)
            auth_login(request, user)
            del request.session['user_id']
            del request.session['otp_code']
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP code.')

    return render(request, 'UserManagement/two_factor_authenticate.html')

@login_required
def setup_2fa(request):
    user = request.user
    if request.method == 'POST':
        device, created = TOTPDevice.objects.get_or_create(user=user, name='default')
        if created:
            messages.success(request, '2FA setup complete.')
        else:
            messages.info(request, '2FA is already set up.')
        return redirect('home')
    return render(request, 'UserManagement/setup_2fa.html')

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
            auth_login(request, user)
            return redirect('setup_2fa')
    else:
        form = UserRegistrationForm()
    return render(request, 'UserManagement/register.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'UserManagement/home.html', {
        'user': request.user,
    })