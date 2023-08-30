from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def custom_datetime_display(datetime):
    if datetime.date() == timezone.now().date():
        return datetime.strftime('%H:%M')
    else:
        return datetime.strftime('%Y-%m-%d')