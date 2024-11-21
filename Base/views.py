from django.shortcuts import render
from .models import HomePage

# Create your views here.


def home_page(request):
    home_page = None # HomePage.objects.get(is_active = True)
    context = {
        'home_page' : home_page
    }
    return render(request , 'Base/home_page.html', context)

def unauth_error(request):
    return render(request , 'Base/unauth_error.html')

