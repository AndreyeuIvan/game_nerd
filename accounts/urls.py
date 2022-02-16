from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.signin,name="home"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.signup,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='main'),name="logout"),
]