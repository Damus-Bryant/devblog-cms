from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # User role choices
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('viewer', 'Viewer'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='viewer')

    def __str__(self):
        return f"{self.username} ({self.role})"