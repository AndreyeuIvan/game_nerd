from django.urls import path
from games.views import main, detail


urlpatterns = [
    path('', main, name='main'),
    path('detail/', detail, name='detail')
]
