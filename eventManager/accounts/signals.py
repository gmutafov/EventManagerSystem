from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from eventManager import settings
from eventManager.accounts.models import AppUser


@receiver(post_save, sender=AppUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Welcome to Event Manager",
            message=f"Hi {instance.first_name},\n\nThank you for signing up for the Event Manager! Explore and register for exciting events.",
            from_email=settings.SENDER_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )