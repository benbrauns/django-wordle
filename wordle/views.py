from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    text = "Home"
    context = {
        'context_text':text,
    }
    return render(request, 'home.html', context)

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