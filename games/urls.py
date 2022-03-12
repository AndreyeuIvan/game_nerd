from django.urls import path, include

from rest_framework import routers

from games.views import main, detail, favorite, like, GameViewSet, search


app_name = "games"

router = routers.DefaultRouter()
router.register(r"viewset", GameViewSet)

urlpatterns = [
    path("", main, name="main"),
    path("like/", like, name="like"),
    path("detail/<int:id>/", detail, name="detail"),
    path("favorite/", favorite, name="favorite"),
    path("api/", include(router.urls)),
    path("search/", search, name='search'),
]
