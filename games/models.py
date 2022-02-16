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


class Genres(models.Model):
    name = models.CharField(max_length=250)


class Platforms(models.Model):
    name = models.CharField(max_length=250)


class Twitter(models.Model):
    text = models.CharField(max_length=250)
    twitter_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


class Game(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.CharField(max_length=250, blank=True)
    release_dates = models.DateField(null=True, blank=True)
    rating = models.BigIntegerField(blank=True)
    #genres = models.ForeignKey("Genres", on_delete=models.CASCADE, null=True)
    #platforms = models.ForeignKey("Platforms", on_delete=models.CASCADE, null=True)
    #tweets = models.ForeignKey("Twitter", on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like"
    )

    def __str__(self):
        return self.name
