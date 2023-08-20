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

def talk_room(request, pk): 
    if request.method == 'POST':
        # フォームの内容を取得
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            # フォームの内容を保存
            messageform.save(sender=request.user, reciever=CustomUser.objects.get(pk=pk))
            print('わあ')
            return redirect('talk_room', pk)
    else:
        messageform = MessageForm()

    frommetohim = Message.objects.filter(sender=pk, receiver=request.user)
    fromhimtome = Message.objects.filter(sender=request.user, receiver=pk)
    all = frommetohim | fromhimtome
    sorted = all.order_by('timestamp')

    context = {
        'he': CustomUser.objects.get(pk=pk),
        'messages': sorted,
        'messageform': messageform,
    }
    
    return render(request, "myapp/talk_room.html", context)

def setting(request):
    return render(request, "myapp/setting.html")

def base(request):
    return render(request, "myapp/base.html")