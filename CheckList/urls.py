from django.urls import path
from .views import single_checlist_item_status_view, checklist_item_list_view, create_checklist_item_status_list

urlpatterns = [
    path('checklist/statusitem/<str:pk>', single_checlist_item_status_view, name='single_checlist_item_status_view'),
    path('checklist/statusitemlist/<str:user>', checklist_item_list_view, name='checklist_item_list_view'),
    path('checklist/create/statusitemlist/', create_checklist_item_status_list, name='create_checklist_item_status_list'),
]