from django.forms import ModelForm
from .models import Asset , Debt


class AddAssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['title' , 'type' , 'value' ]

class AddDebtForm(ModelForm):
    class Meta:
        model = Debt
        fields = ['title' , 'type' , 'value' ]