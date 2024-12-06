from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def greeting(user):
    now = datetime.now().hour
    if user.is_authenticated:
        if now < 12:
            return f"Good morning, {user.first_name}!"
        elif now < 18:
            return f"Good afternoon, {user.first_name}!"
        else:
            return f"Good evening, {user.first_name}!"
    else:
        if now < 12:
            return f"Good morning!"
        elif now < 18:
            return f"Good afternoon!"
        else:
            return f"Good evening!"
