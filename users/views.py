from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout

# Create your views here.
def login(request):
    pass


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
        return redirect('home')