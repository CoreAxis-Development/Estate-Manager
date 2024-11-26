from django.shortcuts import render, redirect
from .models import CheckListItemStatus, CheckListItem, CheckListCategory

def single_checlist_item_status_view(request, pk):
    context = {}
    check_list_item = CheckListItemStatus.objects.get(id=pk)
    context['item'] = check_list_item
    return render(request, 'CheckList/item_view.html', context=context)

def checklist_item_list_view(request, user):
    context = {}
    items = CheckListItemStatus.objects.filter(user=user)
    context['items'] = items
    return render(request, "CheckList/item_list_view.html", context=context)

def create_checklist_item_status_list(request):
    if request.method == 'POST':
        user = request.POST['user_field']
        checklist_items = CheckListItem.objects.all()
        for item in checklist_items:
            temp = CheckListItemStatus.objects.create(user=user, item=item)
            temp.save()
        return redirect('checklist_item_list_view', user)
    return render(request, 'CheckList/create_status_items_view.html')
