from django.forms import ModelForm
from .models import CheckListItemStatus


class UpdateCheckListItemStatus(ModelForm):
    class Meta:
        model = CheckListItemStatus
        fields = ['status']