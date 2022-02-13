# from django.contrib.auth.models import AbstractBaseUser
from audioop import maxpp
from django.db import models

# from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.urls import reverse


"""
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
"""


class Game(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="like"
    )
    like_count = models.BigIntegerField(default="0")

    def __str__(self):
        return self.name


class Favorite(models.Model):
    game = models.ForeignKey(Game, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game.name
