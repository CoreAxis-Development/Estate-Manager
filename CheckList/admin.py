from django.contrib import admin
from .models import CheckListCategory , CheckListItem , CheckListItemStatus
# Register your models here.

admin.site.register(CheckListCategory)
admin.site.register(CheckListItem)
admin.site.register(CheckListItemStatus)