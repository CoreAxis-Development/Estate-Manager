from django.shortcuts import render , redirect
from .models import Asset , Debt
from .forms import AddAssetForm , AddDebtForm
# Create your views here.

def asset_list_view(request , user):
    context = {}
    assets = Asset.objects.filter(user = user)

    if request.method == 'POST':
        form = AddAssetForm(request.POST or None)
        if form.is_valid():
            asset = form.save(commit=False)
            asset.user = user
            asset.save()
            return redirect('asset_list_view')
    context['assets'] = assets
    context['user'] = user
    context['form'] =  AddAssetForm()

    return render(request , "AssetManager/asset_list_view.html", context=context)


def debt_list_view(request , user):
    context = {}
    debts = Debt.objects.filter(user = user)
    if request.method == 'POST':
        form = AddDebtForm(request.POST or None)
        if form.is_valid():
            debt = form.save(commit=False)
            debt.user = user
            debt.save()
            return redirect('debt_list_view')
    context['debts'] = debts
    context['user'] = user
    context['form'] =  AddDebtForm()

    return render(request , "AssetManager/debt_list_view.html", context=context)