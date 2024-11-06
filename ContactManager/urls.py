from django.urls import path 

from .views import (contact_list_view)

urlpatterns = [
    path('contact/listview/<str:user>' ,contact_list_view, name='contact_list_view'),

]