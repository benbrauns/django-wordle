from django.shortcuts import render
from django.http import HttpResponse
from . import models as m
import uuid
import json
import random



# Create your views here.
def home_view(request, *args, **kwargs):
    text = "Home"
    context = {
        'context_text':text,
    }
    return render(request, 'game.html', context)

def wordle_home_view(request, *args, **kwargs):
    text = "Wordle"
    context = {
        'context_text':text,
    }
    return render(request, 'game.html', context)

def nflsub_home_view(request, *args, **kwargs):
    text = "Wordle"
    context = {
        'context_text':text,
    }
    return render(request, 'home.html', context)

def api_home(request, test):
    return HttpResponse('<h1> This is a test </h1>')

def api_get_uuid(request):
    var = uuid.uuid4()
    new = m.User(id=var)
    new.save()
    return HttpResponse(f"{var}")

def api_get_game(request, user):
    if m.User.objects.filter(id=user).exists():
        user = m.User.objects.filter(id=user)[0]
        var = uuid.uuid4()
        words = list(m.Word.objects.all())
        word = random.choice(words)
        new = m.Game(id=var, player_id=user, total_guesses=0, answer=word.word)
        new.save()
        return HttpResponse(f"{var}")
    elif user == "":
        return HttpResponse("Please include a player UUID")
    else:
        return HttpResponse("User not found")

#g_uess is named this way because i have to refence the field "guess" when creating the new
#record for the guess itself
def api_guess(request, gameid, g_uess):
    if m.Game.objects.filter(id=gameid).exists() and m.Game.objects.filter(id=gameid)[0].total_guesses < 6:
        game = m.Game.objects.filter(id=gameid)[0]
        answer = m.Game.objects.filter(id=gameid).values("answer")[0]["answer"].upper()
        # this gets the previous guess then incriments it. The guess_num is used later for
        # entering the new database record of a guess
        guess_num = m.Game.objects.filter(id=gameid).values("total_guesses")[0]["total_guesses"] + 1
        game.total_guesses = guess_num
        results = []
        answer_copy = list(answer)
        for i, c in enumerate(g_uess.upper()):
            if c == answer[i]:
                results.append("X")
                answer_copy.remove(c)
            elif c in answer:
                results.append("-")
                answer_copy.remove(c)
            else:
                results.append("_")
        new_guess = m.Guess(game_id=game, guess_number=guess_num, guess=g_uess)
        new_guess.save()
        game.save()
        if ''.join(results) == "XXXXX":
            return HttpResponse(f"Game Won!")
        else:
            return HttpResponse(f"{''.join(results)}")
    elif m.Game.objects.filter(id=gameid)[0].total_guesses == 6:
        return HttpResponse(f"Out of guesses, the solution was:{m.Game.objects.filter(id=gameid)[0].answer}")
    else:
        return HttpResponse("Game not found")

def api_addWords(request, w, freq):
    new_word = m.Word(word=w, frequency=freq)
    new_word.save()
    return HttpResponse("")