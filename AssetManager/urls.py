from django.urls import path
from . import views  # Import the views module

from .views import (asset_list_view, debt_list_view, collective_list_view, document_list, document_tab)
from .views import (asset_list_view , debt_list_view , collective_list_view , update_asset)

urlpatterns = [
    path('upload/<int:user_id>/', views.upload_doc, name='upload_doc'),
    path('assest/listview/<str:user>', asset_list_view, name='asset_list_view'),
    path('debt/listview/<str:user>', debt_list_view, name='debt_list_view'),
    path('collective/listview/<str:user>', collective_list_view, name='collective_list_view'),
    path('documents/', document_list, name='document_list'),
    path('documents/<int:user_id>/', document_tab, name='document_tab'),  # Add this line
    path('assest/listview/<str:user>' ,asset_list_view, name='asset_list_view'),
    path('debt/listview/<str:user>' ,debt_list_view, name='debt_list_view'),
    path('asset/update/<str:pk>' ,update_asset, name='update_asset'),
    path('collective/listview/<str:user>' ,collective_list_view, name='collective_list_view'),
]