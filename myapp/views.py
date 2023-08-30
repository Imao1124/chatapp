from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,  LogoutView, PasswordChangeView
from .models import CustomUser, Message
from .forms import SignUpForm, LoginForm, MessageForm

def index(request):
    return render(request, "myapp/index.html")

class signup(CreateView):
    form_class = SignUpForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index') # signup に成功したら index にリダイレクト

class login(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

def friends(request):
    # username と img を取り出す
    friends = CustomUser.objects.all().values('pk', 'username', 'img')
    friends = friends.exclude(pk=request.user.pk) # 自分以外のユーザーを取り出す

    # pkとそれぞれのユーザーとの最新のメッセージを格納
    for friend in friends:
        friend['latest_message'] = Message.get_private_message(request.user, CustomUser.objects.get(username=friend['username'])).last()
        

    context = {
        'friends': friends,
    }

    return render(request, "myapp/friends.html", context)

def talk_room(request, pk): 

    # 送信者の情報を取得
    he = CustomUser.objects.get(pk=pk)

    if request.method == 'POST':
        # フォームの内容を取得
        messageform = MessageForm(request.POST)
        if messageform.is_valid():
            # フォームの内容を保存
            messageform.save(sender=request.user, reciever=he)
            return redirect('talk_room', pk)
    else:
        messageform = MessageForm()

    context = {
        'he': he,
        'messages': Message.get_private_message(request.user, he),
        'messageform': messageform,
    }
    
    return render(request, "myapp/talk_room.html", context)

def setting(request):
    context = {
        'pk': request.user.pk,
    }
    return render(request, "myapp/setting.html", context)

class username_change(UpdateView):
    model = CustomUser
    fields = ['username']
    template_name = 'myapp/username_change.html'
    success_url = reverse_lazy('setting')

class logout(LogoutView):
    template_name = 'myapp/index.html'