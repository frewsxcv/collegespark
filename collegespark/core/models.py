from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # school = models.ForeignKey('School')
    major = models.ForeignKey('Major', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)


class School(models.Model):
    pass


class Major(models.Model):
    pass
