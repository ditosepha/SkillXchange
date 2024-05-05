from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('tutor', 'Tutor'),
        ('student', 'Student'),
    )
    
    role = models.CharField(max_length=20, choices=ROLES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'username'

class SkillClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tutor = models.ForeignKey(CustomUser, related_name='classes_taught', on_delete=models.CASCADE)
    running_times = models.CharField(max_length=150)
    max_students = models.PositiveIntegerField()

class Enrollment(models.Model):
    student = models.ForeignKey(CustomUser, related_name='enrollments', on_delete=models.CASCADE)
    skill_class = models.ForeignKey(SkillClass, related_name='enrollments', on_delete=models.CASCADE)
    Enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'skill_class')


class Review(models.Model):
    student = models.ForeignKey(CustomUser, related_name='reviews_given', on_delete=models.CASCADE)
    skill_class = models.ForeignKey(SkillClass, related_name='reviews', on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField()

    class Meta:
        unique_together = ('student', 'skill_class')
