from .models import Customer , Staff , CustomUser

from django.shortcuts import get_object_or_404


def is_valid_user(request , user_id):
    user = CustomUser.objects.get(id = user_id)

    if request.user == user:
        return True
    try:
        staff = Staff.objects.get(user = request.user)
        customer = Customer.objects.get(user = user )
    except:
        return False
    
    if request.user.role == CustomUser.RoleChoices.ADMIN:
        return True

    if customer in staff.assinged_customer.all():
        return True
    

    return False