

def is_allowed_user(request , check_list_item):
    return request.user == check_list_item.user

