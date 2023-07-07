from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    img = models.ImageField()

    class Meta:
        verbose_name = 'CustomUser'

class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Message'