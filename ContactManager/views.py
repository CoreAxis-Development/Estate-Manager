from django.shortcuts import render
from .models import Contact , ContactType
# Create your views here.


def contact_list_view(request , user):
    context = {}
    contacts = []
    types = ContactType.objects.all()
    all_contacts = Contact.objects.filter(user = user)

    for typ in types:
        c_ele = {"title" : typ, 'items' : []}
        for contact in all_contacts:
            if typ in contact.type:
                c_ele['items'].append(contact)
        contacts.append(c_ele)
    context['contacts'] = contacts
    print(context)
    return render(request , 'ContactManager/list_view.html',context)