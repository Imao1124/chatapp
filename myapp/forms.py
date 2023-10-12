from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Message
from django.utils import timezone

from allauth.account.forms import SignupForm    

class CustomSignupForm(SignupForm):

    icon = forms.ImageField(label='アイコン', required=True)
    class Meta:
        model = CustomUser

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
    def signup(self, request, user):
        user.img = self.cleaned_data['icon']
        user.save()
        return user


# class SignUpForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2', 'img')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'ユーザー名を入力してください'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワードを入力してください'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text',)

    def save(self, sender, reciever, commit=True):
        message = super().save(commit=False)
        message.sender = sender
        message.receiver = reciever
        message.timestamp = timezone.now()
        if commit:
            message.save()
        return message