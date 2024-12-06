from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()
    available_from = models.DateTimeField()

    def __str__(self):
        return self.name


class Organizer(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
