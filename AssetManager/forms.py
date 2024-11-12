# forms.py
from django.forms import ModelForm
from .models import Asset, Debt, Doc

class AddAssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['title', 'type', 'value']

class AddDebtForm(ModelForm):
    class Meta:
        model = Debt
        fields = ['title', 'type', 'value']

class DocForm(ModelForm):
    class Meta:
        model = Doc
        fields = ['doc_type', 'file']