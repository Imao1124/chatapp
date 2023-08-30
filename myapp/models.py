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
    timestamp = models.DateTimeField()

    class Meta:
        verbose_name = 'Message'

    # お互いのメッセージを取得して並び替え
    def get_private_message(me, he):
        frommetohim = Message.objects.filter(sender=he, receiver=me)
        fromhimtome = Message.objects.filter(sender=me, receiver=he)
        all = frommetohim | fromhimtome
        sorted = all.order_by('timestamp')
        return sorted