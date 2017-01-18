from django.db import models
from django.contrib.auth.models import User
from .usertypes import USER_CHOICES
from cloudinary.models import CloudinaryField


# Model to Store the user details
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = CloudinaryField('picture', blank=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES, default='P')

    class Meta:
        db_table = "UserProfile"

    def __str__(self):
        return self.user.username


# model to store game uploads
class Game(models.Model):
    name = models.TextField(help_text="Please specify your game name")
    description = models.TextField(max_length=250)
    logo = CloudinaryField('logo', blank=True)
    resource_info = models.URLField(help_text="Please specify the URL")
    cost = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    upload_date = models.DateTimeField(auto_now_add=True)
    developer = models.ForeignKey(User, related_name='uploaded_games', on_delete=models.CASCADE)

    class Meta:
        db_table = "Game"
        ordering = ['upload_date']

    def __str__(self):
        return self.name


# Purchase information
class Purchase(models.Model):
    game_details = models.ForeignKey(Game, related_name='game_details', on_delete=models.CASCADE)
    player_details = models.ForeignKey(User, related_name='player_details', on_delete=models.CASCADE)
    cost = models.DecimalField(default=0.0, decimal_places=2, max_digits=10)
    purchase_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Purchase"
        ordering = ['purchase_date']

    def __str__(self):
        return self.purchase_date


# store scores history
class Score(models.Model):
    game_info = models.ForeignKey(Game, related_name='game_info', on_delete=models.CASCADE)
    player_info = models.ForeignKey(User, related_name='player_info', on_delete=models.CASCADE)
    last_played = models.DateTimeField(auto_now=True)
    score = models.BigIntegerField(default=0)

    class Meta:
        db_table = "Score"
        ordering = ['last_played']

    def __str__(self):
        self.last_played


# store state of the previous action
class GameState(models.Model):
    game = models.ForeignKey(Game, related_name='game_state', on_delete=models.CASCADE)
    player = models.ForeignKey(User, related_name='player_state', on_delete=models.CASCADE)
    app_state = models.TextField(blank=True, max_length=500)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "GameState"
        ordering = ['last_modified']
        unique_together = ('game', 'player')

    def __str__(self):
        return self.last_modified
