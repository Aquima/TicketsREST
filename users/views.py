from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.contrib.auth.models import User

from users.serializer import SignUpSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticated,)


# Create your views here.
def login(request):
    pass


def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
        return redirect('home')


