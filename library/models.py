from django.db import models
from games.models import Game
from users.models import CustomUser
# Create your models here.

class LibraryGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Игра в библиотеке"
        verbose_name_plural ="Игры в библиотеке"

    def __str__(self):
        return f"{self.user.username} - {self.game.title}"

