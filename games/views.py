from django.shortcuts import render


def main(request):
    return render(request, 'games/main.html')

def detail(request):
    """
    Добавить айди для переменной
    try:
        game = Game.objects.get(pk=poll_id)
    except Game.DoesNotExist:
        return render(request, 'polls/404.html')
    """
    return render(request, 'games/detail.html',)