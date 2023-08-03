from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .models import CustomUser, Message
from .forms import SignUpForm, LoginForm, MessageForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

def index(request):
    return render(request, "myapp/index.html")

class signup_view(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index') # signup に成功したら index にリダイレクト

class login(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

def friends(request):
    # username と img を取り出す
    friends = CustomUser.objects.all().values('username', 'img')
    context = {
        'friends': friends,
    }
    return render(request, "myapp/friends.html", context)

class talk_room(CreateView):
    form_class = MessageForm
    model = Message
    template_name = 'myapp/talk_room.html'

    def get_context_data(self, **kwargs):
        pk:int=self.kwargs['pk']
        print(pk)
        return super().get_context_data(**kwargs)
    

    def get_messages(self, pk):
        return Message.objects.filter(sender=pk, receiver=self.request.user)

def setting(request):
    return render(request, "myapp/setting.html")

def base(request):
    return render(request, "myapp/base.html")