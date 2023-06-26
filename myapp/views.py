from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import SignUpForm
from django.urls import reverse_lazy

def index(request):
    return render(request, "myapp/index.html")

class signup_view(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index')

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