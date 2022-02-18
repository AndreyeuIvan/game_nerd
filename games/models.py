# from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.forms import CharField, DateTimeField

# from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings


"""
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
"""


class Genre(models.Model):
    created_at = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    updated_at = models.CharField(max_length=250)
    url = models.URLField()
    checksum = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Twitter(models.Model):
    text = models.CharField(max_length=500)
    _id = models.CharField(max_length=250)  # models.BigIntegerField(blank=True)
    created_at = models.CharField(
        max_length=250
    )  # models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text
        

class Game(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True, max_length=500)
    summary = models.CharField(max_length=1500, blank=True, null=True)
    release_dates = models.CharField(
        max_length=250, blank=True, null=True
    )  # models.DateField(null=True, blank=True)
    rating = models.BigIntegerField(blank=True, null=True)
    genres = models.ManyToManyField("Genre", related_name="genres")
    platforms = models.ManyToManyField("Platform", related_name="platforms" )
    tweets = models.ManyToManyField("Twitter", related_name="tweets")
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like"
    )

    def __str__(self):
        return self.name
