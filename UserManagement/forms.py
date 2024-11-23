# UserManagement/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True , label= 'Email Address')
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.label  # Use the label as the placeholder
            field.widget.attrs['class'] = 'form-control underline-text-field'  # Add any additional classes
            field.label = ''  # Hide the label
        
class OTPVerificationForm(forms.Form):
    otp_token = forms.CharField(max_length=6, required=True, label='OTP Token')