from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Message
from django import forms
from django.utils import timezone

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'img')

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

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