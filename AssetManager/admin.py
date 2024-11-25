from django.contrib import admin
from .models import AssetType , Asset , Debt , DebtType, DocType
# Register your models here.
admin.site.register(Asset)
admin.site.register(AssetType)
admin.site.register(Debt)
admin.site.register(DebtType)
admin.site.register(DocType)