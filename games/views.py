from games.models import Game
from games.serializers import GameSerializer

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

from rest_framework import viewsets


def main(request):
    """
    Отображаем все имеющееся игры в базе
    """
    game = Game.objects.all()
    paginator = Paginator(game, 15)
    page_number = request.GET.get('page')
    games = paginator.get_page(page_number)
    context = {"games": games}
    return render(request, "games/main.html", context)


def detail(request, id):
    """
    Предоставляем детали игры
    """
    context = {"game": get_object_or_404(Game, pk=id)}
    return render(request, "games/detail.html", context)


def search(request):
    """Search query by game name."""
    query = request.GET.get('q')
    result = Game.objects.filter(Q(name__icontains=query))
    try:
        return detail(request, id=result.values()[0].get('id'))
    except IndexError:
        return main(request)


def favorite(request):
    """
    Возвращаем игры с лайками
    """
    user = request.user.id
    games = Game.objects.filter(likes=user)
    context = {"games": games}
    return render(request, "games/main.html", context)


@login_required
def like(request):
    """
    Создаем лайки
    """
    if request.method == "GET":
        game_id = request.GET["game_id"]
        likedgame = get_object_or_404(Game, id=game_id)
        if likedgame.likes.filter(id=request.user.id).exists():
            likedgame.likes.remove(request.user.id)
            likedgame.save()
            return HttpResponse("remove")
        else:
            likedgame.likes.add(request.user.id)
            likedgame.save()
        return HttpResponse("success")
    else:
        return HttpResponse("unsuccesful")


class GameViewSet(viewsets.ModelViewSet):
    """
    Created api with 2 methods: get by id and list
    """
    serializer_class = GameSerializer
    queryset = Game.objects.all()
