from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("games.urls")),
<<<<<<< HEAD
    path("accounts/", include("allauth.urls")),
=======
>>>>>>> parent of f0fc85f (created sign up and sign in)
]
