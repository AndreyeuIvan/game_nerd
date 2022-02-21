from games.models import Game

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def main(request):
    """
    Отображаем все имеющееся игры в базе
    """
    # context = {"games": IG.get_games_list()}
    context = {"games": Game.objects.all()}
    return render(request, "games/main.html", context)


def detail(request, id):
    """
    Предоставляем детали игры
    """
    context = {"game": get_object_or_404(Game, pk=id)}
    return render(request, "games/detail.html", context)


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
