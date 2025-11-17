from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="avatars",default="default.jpg",verbose_name="Аватарка" )
    bio = models.TextField(blank = True,verbose_name="О себе")
    comment_count  = models.IntegerField(default=0,verbose_name="Кол-во комментов")
    last_visit = models.DateTimeField(auto_now=True,verbose_name="Последний визит")

    is_staff = models.BooleanField(default=False,verbose_name="Доступ к админ-панели")
    is_superuser = models.BooleanField(default=False,verbose_name="Хозяин сайта?" )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

