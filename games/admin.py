from django.contrib import admin
from games.models import Game, Genres, Twitter, Platforms


admin.site.register(Game)
admin.site.register(Genres)
admin.site.register(Platforms)
admin.site.register(Twitter)
