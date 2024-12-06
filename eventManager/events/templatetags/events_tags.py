from django import template


register = template.Library()

@register.filter
def format_event_date(value):
    return value.strftime('%A, %d %B %Y')
