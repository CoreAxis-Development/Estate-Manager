# UserManagement/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        
class OTPVerificationForm(forms.Form):
    otp_token = forms.CharField(max_length=6, required=True, label='OTP Token')