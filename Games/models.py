from django.db import models

# Create your models here.

class GameSession(models.Model):
    game_status = models.CharField(max_length=20, default='waiting')  # 'waiting', 'playing', 'finished
    created_at = models.DateTimeField(auto_now_add=True)
    last_word = models.CharField(max_length=100,blank=True, null=True)
    current_player = models.ForeignKey('Word_Chain_player', on_delete=models.CASCADE, null=True, blank=True)
    winner = models.ForeignKey('Word_Chain_player', on_delete=models.CASCADE, null=True, blank=True, related_name='winner')

    def __str__(self):
        return self.game_status



class Word_Chain_player(models.Model):
    player_name = models.CharField(max_length=100)
    player_status = models.CharField(max_length = 10, default='waiting')  # 'waiting', 'playing', 'finished'
    game_session_joined = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='players')
    player_turn_order = models.IntegerField(default=0)  # To determine the order of players in the game 
    def __str__(self):
        return self.player_name

class Word_Chain_words(models.Model):
    word_provided = models.CharField(max_length=100)
    player_who_provided = models.ForeignKey(Word_Chain_player, on_delete=models.CASCADE, related_name='words_provided')
    word_used_already =models.BooleanField(default=False)  # To check if the word has been used already in the game
    word_game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE, related_name='words_used') 

    def __str__(self):
        return self.word_provided
