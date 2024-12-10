from asgiref.sync import sync_to_async
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from eventManager import settings
from eventManager.accounts.models import AppUser


@receiver(post_save, sender=AppUser)
async def create_profile(sender, instance, created, **kwargs):
    if created:
        email = EmailMessage(
            subject="Welcome to Event Manager",
            body=f"Hi {instance.first_name},\n\nThank you for signing up for the Event Manager! Explore and register for exciting events.",
            from_email=settings.SENDER_EMAIL,
            to=[instance.email],
        )
        await sync_to_async(email.send)(fail_silently=False)