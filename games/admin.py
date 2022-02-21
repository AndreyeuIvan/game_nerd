from django.contrib import admin
from games.models import Game, Genre, Twitter, Platform


admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Twitter)
