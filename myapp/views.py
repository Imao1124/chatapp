from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import CustomUser

def index(request):
    return render(request, "myapp/index.html")

class signup_view(CreateView):
    model = CustomUser
    fields = ['username', 'email', 'password', 'img']
    template_name = 'myapp/signup.html'

def login_view(request):
    return render(request, "myapp/login.html")

def friends(request):
    return render(request, "myapp/friends.html")

def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")

def base(request):
    return render(request, "myapp/base.html")