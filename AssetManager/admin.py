from django.contrib import admin
from .models import AssetType , Asset , Debt , DebtType
# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(Debt)
admin.site.register(DebtType)