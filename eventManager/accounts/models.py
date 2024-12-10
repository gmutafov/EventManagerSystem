from django.contrib.auth.models import AbstractUser
from django.db import models

from eventManager.accounts.validators import validate_capitalized, only_letters



class AppUser(AbstractUser):
    first_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[validate_capitalized,
                    only_letters]
    )
    last_name = models.CharField(
        max_length=50,
        blank=True,
        validators=[validate_capitalized,
                    only_letters]
    )
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


