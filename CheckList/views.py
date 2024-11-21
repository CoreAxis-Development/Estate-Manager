from django.shortcuts import render, redirect ,get_object_or_404
from .models import CheckListItemStatus, CheckListItem, CheckListCategory
from UserManagement.models import CustomUser
from .helper import is_allowed_user
from .forms import UpdateCheckListItemStatus
from UserManagement.decorators import allowed_users
from django.contrib.auth.decorators import login_required

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def single_checlist_item_status_view(request, pk):
    context = {}
    check_list_item = CheckListItemStatus.objects.get(id=pk)
    all_item = CheckListItemStatus.objects.filter(user = check_list_item.user)
    next_item = check_list_item
    prev_item = check_list_item
    item_reached = False
    for item in all_item:
        if item_reached :
            next_item = item
            break
        if item == check_list_item :
            item_reached = True
        
        if not item_reached:
            prev_item = item
        
        
    
    if is_allowed_user(request , check_list_item):
        context['item'] = check_list_item
        context['nitem'] = next_item
        context['pitem'] = prev_item
        context['user'] = check_list_item.user
        return render(request, 'CheckList/item_view.html', context=context)
    else :
        return redirect('unauth_error')

@login_required
def checklist_item_list_view_self(request):
    context = {}
    items = CheckListItemStatus.objects.filter(user=request.user)
    context['items'] = items
    return render(request, "CheckList/item_list_view.html", context=context)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def checklist_item_list_view(request, user):
    context = {}
    user = CustomUser.objects.get(id = user)
    items = CheckListItemStatus.objects.filter(user=user)
    context['items'] = items
    context['user'] = user
    return render(request, "CheckList/item_list_view.html", context=context)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def create_checklist_item_status_list(request , user):
   
    user = CustomUser.objects.get(id = user)
    checklist_items = CheckListItem.objects.all()
    for item in checklist_items:
        temp = CheckListItemStatus.objects.create(user=user, item=item)
        temp.save()
    return redirect('checklist_item_list_view', user.id)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def update_checklist_item(request , pk):
    item = get_object_or_404(CheckListItemStatus, pk=pk)  # Fetch the record
    if request.method == "POST":
        form = UpdateCheckListItemStatus(request.POST, instance=item)  # Bind data to the form
        if form.is_valid():
            form.save()  # Save updated record
            return redirect('checklist_item_list_view' , item.user.id)  # Redirect after successful update
    else:
        form = UpdateCheckListItemStatus(instance=item)  # Pre-fill form with existing data
    return render(request, 'CheckList/update_checklist_items.html', {'form': form})
    
   
