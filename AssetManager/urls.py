from django.urls import path 

from .views import (asset_list_view , debt_list_view , collective_list_view , update_asset)

urlpatterns = [
    path('assest/listview/<str:user>' ,asset_list_view, name='asset_list_view'),
    path('debt/listview/<str:user>' ,debt_list_view, name='debt_list_view'),
    path('asset/update/<str:pk>' ,update_asset, name='update_asset'),
    path('collective/listview/<str:user>' ,collective_list_view, name='collective_list_view'),
]