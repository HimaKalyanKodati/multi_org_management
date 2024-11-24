from django.http import HttpResponse

#models
from .models import UserExtend

#decorator is used to restrict the CRUD operations based on role
def role_required(allowed_roles):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            role_name = str(UserExtend.objects.get(user = request.user).role)
            if role_name not in allowed_roles:
                return HttpResponse(f"<h2>your role is {role_name} you don't have access to this resource please contact your admin!</h2>")
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator