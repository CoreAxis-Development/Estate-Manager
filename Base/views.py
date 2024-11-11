from django.shortcuts import render

# Create your views here.


def unauth_error(request):
    return render(request , 'Base/unauth_error.html')