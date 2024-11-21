from UserManagement.models import Staff , Customer , CustomUser

def is_allowed_user(request , check_list_item):
    
    return True#return request.user == check_list_item.user

