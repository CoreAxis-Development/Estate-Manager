from django import forms
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

class DocForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Doc
        fields = ['doc_type', 'file']