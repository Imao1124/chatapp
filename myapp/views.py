from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Message
from .forms import CustomSignupForm, LoginForm, MessageForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "myapp/index.html")

class signup(CreateView):
    form_class = CustomSignupForm
    model = CustomUser
    template_name = 'myapp/signup.html'
    success_url = reverse_lazy('index') # signup に成功したら index にリダイレクト

    def form_valid(self, form):
        logger.info('User {} signed up'.format(form.cleaned_data['username']))
        return super().form_valid(form)

class login(LoginView):
    form_class = LoginForm
    template_name = 'myapp/login.html'

@login_required
def friends(request):
    # username と img を取り出す
    friends = CustomUser.objects.all().values('pk', 'username', 'img')
    friends = friends.exclude(pk=request.user.pk) # 自分以外のユーザーを取り出す

    query = request.GET.get('query')

    print(query)

    if query:
        friends = friends.filter(username__icontains=query)

    # pkとそれぞれのユーザーとの最新のメッセージを格納
    for friend in friends:
        friend['latest_message'] = Message.get_private_message(request.user, CustomUser.objects.get(username=friend['username'])).last()
        
    context = {
        'friends': friends,
    }

    return render(request, "myapp/friends.html", context)

@login_required
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

@login_required
def setting(request):
    context = {
        'pk': request.user.pk,
    }
    return render(request, "myapp/setting.html", context)

class username_change(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['username']
    template_name = 'myapp/username_change.html'
    success_url = reverse_lazy('setting')

class email_change(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['email']
    template_name = 'myapp/email_change.html'
    success_url = reverse_lazy('setting')

class icon_change(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['img']
    template_name = 'myapp/icon_change.html'
    success_url = reverse_lazy('setting')

class password_change(LoginRequiredMixin, PasswordChangeView):
    template_name = 'myapp/password_change.html'
    success_url = reverse_lazy('setting')

class logout(LogoutView):
    template_name = 'myapp/index.html'