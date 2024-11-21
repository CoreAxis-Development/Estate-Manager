from django.shortcuts import render , redirect , get_object_or_404
from .models import Contact , ContactType
from UserManagement.models import CustomUser
from .forms import ContactSaveForm
from UserManagement.decorators import allowed_users
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def contact_list_view(request , user):
    context = {}
    contacts = []
    types = ContactType.objects.all()
    all_contacts = Contact.objects.filter(user = user)
 

    if request.method == "POST":
        form = ContactSaveForm(request.POST or None)
        if form.is_valid():
            contact = form.save()
            
            contact.user = user
            contact.save()
            return redirect('contact_list_view',user)

    for typ in types:
        c_ele = {"title" : typ, 'items' : []}
        for contact in all_contacts:
            print(contact , " -> " ,contact.type.all())
            if typ in contact.type.all():
                c_ele['items'].append(contact)
        contacts.append(c_ele)
    context['contacts'] = contacts
    context['user'] = CustomUser.objects.get(id = user)
    context['form'] = ContactSaveForm()

    return render(request , 'ContactManager/list_view.html',context)

@login_required
@allowed_users(allowed_roles=[CustomUser.RoleChoices.EXECUTOR , CustomUser.RoleChoices.ADMIN , CustomUser.RoleChoices.CUSTOMER])
def update_contact_view(request , pk):
    contact = get_object_or_404(Contact , id =  pk)
    if request.method == 'POST':
        form = ContactSaveForm(request.POST , instance=contact)
    return render(request , "")