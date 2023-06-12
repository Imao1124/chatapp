from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    img = models.ImageField()

    class Meta:
        verbose_name = 'CustomUser'


# パスワード2回目の入力をどう実装するか