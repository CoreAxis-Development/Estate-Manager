from UserManagement.models import Staff , Customer , CustomUser

def is_allowed_user(request , check_list_item):
    # if request.user.role != CustomUser.RoleChoices.CUSTOMER:
    #     emp = Staff.objects.get(user = request.user)
    
    return True#return request.user == check_list_item.user

