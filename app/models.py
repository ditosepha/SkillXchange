from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('tutor', 'Tutor'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=20, choices=ROLES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)