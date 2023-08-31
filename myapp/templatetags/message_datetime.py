from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def custom_datetime_display(datetime):
    if not datetime:
        return ''
    if datetime.date() == timezone.now().date():
        return datetime.strftime('%H:%M')
    elif datetime.year == timezone.now().year:
        return datetime.strftime('%m-%d')
    else:
        return datetime.strftime('%Y-%m-%d')