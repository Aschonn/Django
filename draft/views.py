from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Year, Player
from draft.forms import SubmitMock

# Create your views here.

#Notes:
    #this will require a form
    #double underscore is very important
    #child to parent
    #players = Player.objects.filter(year__year=2020)
    #ex) <QuerySet [<Player: Anthony Edwards>, <Player: Lamelo Ball>]>
    #parent to Child
    # Year.objects.filter(player__year=2020)
    #ex) [<Year: Year object (2020)>, <Year: Year object (2020)>]>


def mockdraft(request):
    players = Player.objects.filter(classof='2020').order_by('year_rank')
    form = SubmitMock()
    context = {
        "players" : players,
        "form" : form,
        "title" : "Draft",
    }

    if request.method == 'POST':
        form = SubmitMock(request.POST)
        if form.is_valid():
            message = form.cleaned_data['mock']
            players = Player.objects.filter(classof=message).order_by('year_rank')
            context = {'players': players, 'form': form, "title" : "Draft"}
            messages.success(request, f'{message} Mock Draft')
            return render(request, 'draft/mockdraft.html', context)


    return render(request, 'draft/mockdraft.html', context)
