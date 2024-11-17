from django.shortcuts import redirect

def allowed_users(allowed_roles= []):
    def decorator(view_func):
        def wrapper(request , *args, **kwargs):
            #print(allowed_roles)
            group = None
            role = request.user.role
            #print(role)
            
            if role in allowed_roles:
                return view_func(request , *args, **kwargs)
            else :
                #print('User Not allowed')
                
                return redirect('unauth_error')
        return wrapper
    return decorator