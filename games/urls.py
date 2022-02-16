from django.urls import path, re_path

from games.views import main, detail, favorite, like, test

app_name = "games"

urlpatterns = [
    path("", test, name="main"),
    path("like/", like, name="like"),
    path("detail/<int:id>/", detail, name="detail"),
    path("favorite/", favorite, name="favorite"),
]
