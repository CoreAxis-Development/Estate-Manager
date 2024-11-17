from django.shortcuts import render, redirect
from .models import CheckListItemStatus, CheckListItem, CheckListCategory
from UserManagement.models import CustomUser
from .helper import is_allowed_user


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
        return render(request, 'CheckList/item_view.html', context=context)
    else :
        return redirect('unauth_error')


def checklist_item_list_view_self(request):
    context = {}
    items = CheckListItemStatus.objects.filter(user=request.user)
    context['items'] = items
    return render(request, "CheckList/item_list_view.html", context=context)

def checklist_item_list_view(request, user):
    context = {}
    items = CheckListItemStatus.objects.filter(user=user)
    context['items'] = items
    return render(request, "CheckList/item_list_view.html", context=context)


def create_checklist_item_status_list(request , user):
   
    user = CustomUser.objects.get(id = user)
    checklist_items = CheckListItem.objects.all()
    for item in checklist_items:
        temp = CheckListItemStatus.objects.create(user=user, item=item)
        temp.save()
    return redirect('checklist_item_list_view', user.id)
   
