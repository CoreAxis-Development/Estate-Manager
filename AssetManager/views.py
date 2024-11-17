from django.shortcuts import render , redirect
from .models import Asset , Debt
from .forms import AddAssetForm , AddDebtForm
from UserManagement.models import CustomUser
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
            return redirect('asset_list_view' , user)
        
    user = CustomUser.objects.get(id = user)
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
            return redirect('debt_list_view' , user)
    
    user = CustomUser.objects.get(id = user)
    context['debts'] = debts
    context['user'] = user
    context['form'] =  AddDebtForm()

    return render(request , "AssetManager/debt_list_view.html", context=context)


def collective_list_view(request , user):
    context = {}
    assets = Asset.objects.filter(user = user)
    debts = Debt.objects.filter(user = user)
    context['assets'] = assets
    context['debts'] = debts

    total = 0
    for asset in assets:
        total += asset.value
    for debt in debts:
        total -= debt.value
    context['total'] = total
    user = CustomUser.objects.get(id = user)
    context['user'] = user

    return render(request,"AssetManager/collective_list_view.html",context = context)