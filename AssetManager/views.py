from django.shortcuts import render , redirect
from .models import Asset , Debt, Doc
from .forms import AddAssetForm , AddDebtForm, DocForm
from UserManagement.models import CustomUser
from UserManagement.decorators import allowed_users
from django.contrib.auth.decorators import login_required
import logging
logger = logging.getLogger(__name__)

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


@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR, CustomUser.RoleChoices.ADMIN, CustomUser.RoleChoices.CUSTOMER])
def document_list(request):
    documents = Doc.objects.filter(user=request.user)
    return render(request, 'AssetManager/document_list.html', {'documents': documents})
@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR, CustomUser.RoleChoices.ADMIN, CustomUser.RoleChoices.CUSTOMER])
def upload_doc(request, user_id):
    success = False
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = CustomUser.objects.get(id=user_id)
            doc.save()
            logger.info(f"Document {doc.file.name} uploaded successfully to {doc.file.url}")
            success = True
    else:
        form = DocForm()
    return render(request, 'AssetManager/upload_doc.html', {'form': form, 'success': success})

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR, CustomUser.RoleChoices.ADMIN, CustomUser.RoleChoices.CUSTOMER])
def document_tab(request, user_id):
    documents = Doc.objects.filter(user_id=user_id)
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = CustomUser.objects.get(id=user_id)
            doc.save()
            logger.info(f"Document {doc.file.name} uploaded successfully to {doc.file.url}")
            return redirect('document_tab', user_id=user_id)
    else:
        form = DocForm()
    return render(request, 'AssetManager/document_tab.html', {'documents': documents, 'form': form})