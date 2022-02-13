import site
from django.contrib import admin
from games.models import Favorite, Game

admin.site.register(Favorite)
admin.site.register(Game)
