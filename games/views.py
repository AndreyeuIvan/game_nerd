import imp
from django.shortcuts import render
from games.service_igdb import IG


def main(request):
    context = {"games": IG.get_all()}
    return render(request, "games/main.html", context)


def detail(request, id):
    """
    Добавить айди для переменной
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return render(request, 'games/404.html')
    """
    context = {"games": IG.get_by_id(id)}
    return render(request, "games/detail.html", context)
