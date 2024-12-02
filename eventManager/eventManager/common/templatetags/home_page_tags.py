from datetime import datetime

from django import template

from eventManager.events.models import Event

register = template.Library()

@register.simple_tag
def current_year():
    return datetime.now().year

@register.simple_tag
def total_events():
    return Event.objects.count()