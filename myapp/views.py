from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import SignUpForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, "myapp/index.html")

class signup_view(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index')

class login(LoginView):
    template_name = 'myapp/login.html'
    form_class=LoginForm

def friends(request):
    friends = CustomUser.objects.all().values('username', 'img')
    context = {
        'friends': friends,
    }
    return render(request, "myapp/friends.html", context)

def talk_room(request):
    return render(request, "myapp/talk_room.html")

def setting(request):
    return render(request, "myapp/setting.html")

def base(request):
    return render(request, "myapp/base.html")