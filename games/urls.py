from django.urls import path, re_path

from games.views import main, detail, favorite, like

app_name = "games"

urlpatterns = [
    path("", main, name="main"),
    path("like/", like, name="like"),
    path("detail/<int:id>/", detail, name="detail"),
    path("favorite/", favorite, name="favorite"),
]
