from django.shortcuts import render , redirect , get_object_or_404
from .models import Asset , Debt
from .forms import AddAssetForm , AddDebtForm
from UserManagement.models import CustomUser
from UserManagement.decorators import allowed_users
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def asset_list_view(request , user):
    context = {}
    assets = Asset.objects.filter(user = user)

    if request.method == 'POST':
        form = AddAssetForm(request.POST or None)
        if form.is_valid():
            asset = form.save(commit=False)
            user = CustomUser.objects.get(id = user)
            asset.user = user
            asset.save()
            return redirect('asset_list_view' , user.id)
        
    user = CustomUser.objects.get(id = user)
    context['assets'] = assets
    context['user'] = user
    context['form'] =  AddAssetForm()

    return render(request , "AssetManager/asset_list_view.html", context=context)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def debt_list_view(request , user):
    context = {}
    debts = Debt.objects.filter(user = user)
    if request.method == 'POST':
        form = AddDebtForm(request.POST or None)
        if form.is_valid():
            debt = form.save(commit=False)
            user = CustomUser.objects.get(id = user)
            debt.user = user
            debt.save()
            return redirect('debt_list_view' , user.id)
    
    user = CustomUser.objects.get(id = user)
    context['debts'] = debts
    context['user'] = user
    context['form'] =  AddDebtForm()

    return render(request , "AssetManager/debt_list_view.html", context=context)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
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


def update_asset(request, pk):
    # Retrieve the Asset instance
    asset = get_object_or_404(Asset, id=pk)
    
    if request.method == 'POST':
        # Bind form with POST data and the existing instance
        form = AddAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()  # Save the updated instance
            return redirect('asset_list_view' , asset.user.id)  # Redirect to a success page
    else:
        # Initialize the form with the existing instance
        form = AddAssetForm(instance=asset)
    
    return render(request, 'AssetManager/update_asset.html', {'form': form})