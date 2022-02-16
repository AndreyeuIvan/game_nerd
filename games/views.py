from games.service_igdb import IG, tw
from games.models import Game

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def main(request):
    context = {"games": IG.get_games_list()}
    return render(request, "games/main.html", context)


def test(request):
    """
    Добавить айди для переменной
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return render(request, 'games/404.html')
    """
    context = {"games": Game.objects.all()}
    return render(request, "games/main.html", context)


def detail(request, id):
    """
    Добавить айди для переменной
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        return render(request, 'games/404.html')
    """
    context = {"games": IG.get_game_by_id(id)}
    twitter = {"twitter": tw.get_tweets(context["games"][0]["name"])}
    context |= twitter
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
    if request.method == "GET":
        game_id = request.GET["game_id"]
        likedgame = get_object_or_404(Game, id=game_id)
        if likedgame.likes.filter(id=request.user.id).exists():
            likedgame.likes.remove(request.user.id)
            likedgame.like_count -= 1
            likedgame.save()
            return HttpResponse("remove")
        else:
            likedgame.likes.add(request.user.id)
            likedgame.like_count += 1
            likedgame.save()
        return HttpResponse("success")
    else:
        return HttpResponse("unsuccesful")
