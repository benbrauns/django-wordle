from uuid import uuid4
from django.db import models
# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, null=False, blank=False, editable=False, default=uuid4())
    # games_played = models.IntegerField(default=0)
    # games_won = models.IntegerField(default=0)
    # shortest_game = models.IntegerField(default=0) #in rounds played
    # fastest_game = models.DecimalField(max_digits=10, decimal_places=2) #in seconds

class Game(models.Model):
    id            = models.UUIDField(primary_key=True, null=False, blank=False, editable=False, default=uuid4())
    player_id     = models.ForeignKey(User, on_delete=models.CASCADE)
    total_guesses = models.IntegerField(default=0)
    answer        = models.CharField(max_length=5)
    

class Guess(models.Model):
    game_id           = models.ForeignKey(Game, on_delete=models.CASCADE)
    guess_number = models.IntegerField()
    guess        = models.CharField(max_length=5, null=True, blank=True)

class Word(models.Model):
    word = models.CharField(max_length=5)
    frequency = models.DecimalField(max_digits=5, decimal_places=4)
