from django.contrib.auth.models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = CustomUser
        user = ('username', 'email', 'password', 'img')
