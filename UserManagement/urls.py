
# UserManagement/urls.py
from django.urls import path
from .views import user_list_view, login_view, logout_view, register_view, home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),  # Add this line for the home page
    path('users/', user_list_view, name='user_list_view'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    # Password reset URLs remain the same
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='UserManagement/password_reset.html'), 
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='UserManagement/password_reset_done.html'), 
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='UserManagement/password_reset_confirm.html'), 
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='UserManagement/password_reset_complete.html'), 
        name='password_reset_complete'),
]