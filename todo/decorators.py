from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from functools import wraps



def group_based_redirect(view_func):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.groups.filter(name='user').exists():
                return redirect('user-dashboard')
            elif request.user.groups.filter(name='moderator').exists():
                return redirect('moderator-dashboard')
            elif request.user.groups.filter(name='admin').exists():
                return redirect('admin:index')  # Preusmeri na Django admin stranicu
        return view_func(request, *args, **kwargs)

    return wrapper_function