from django.conf import settings
from django.db import models
from eventManager.accounts.models import AppUser
from eventManager.common.models import Venue, Organizer


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        related_name='events'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.URLField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='events')
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE, related_name='events')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ["date"]


class Registration(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='registrations'
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='registrations'
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"

    class Meta:
        unique_together = ('user', 'event')
