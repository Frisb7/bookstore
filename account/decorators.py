from django.shortcuts import redirect
from django.contrib import messages

def allowed_users(perms=[]) :
    def decorator(view_func) :
        def wrapper_func(request, *args, **kwargs) :
            if ('superuser' in perms) and (request.user.is_superuser) :
                return(view_func(request, *args, **kwargs))
            else :
                if ('admin' in perms) and (request.user.is_admin) :
                    return(view_func(request, *args, **kwargs))
                else:
                    if ('staff' in perms) and (request.user.is_staff) :
                        return(view_func(request, *args, **kwargs))
                    else:
                        if ('customer' in perms) and (request.user.is_customer) :
                            return(view_func(request, *args, **kwargs))
                        else:
                            return(redirect('unauth'))
                        return(redirect('unauth'))
                    return(redirect('unauth'))
        return(wrapper_func)
    return(decorator)