import imp
from django.shortcuts import render
from games.service_igdb import IG, tw


def main(request):
    context = {"games": IG.get_games_list()}
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
    # import pdb;pdb.set_trace()
    return render(request, "games/detail.html", context)
