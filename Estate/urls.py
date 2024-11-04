# Estate/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CheckList.urls')),
    path('', include('AssetManager.urls')),
    path('', include('UserManagement.urls')),
]