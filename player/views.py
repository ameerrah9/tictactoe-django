from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from gameplay.models import Game
from player.forms import InvitationForm


@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user.id)
    active_games = my_games.active()

    # Important to understand hwo many queries are actually ran for this
    # Lazy query sets are only updated when they actually get used

    # all_my_games = list(games_first_player) + \
    #                 list(games_second_player)

    return render(request, "player/home.html", {'games': active_games})

@login_required
def new_invitation(request):
    if request.method == 'POST':
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('player:home')
    else:
        form = InvitationForm()
    return render(request, "player/new_invitation.html", {'form': form})
