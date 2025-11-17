from django.db import models
from django.utils.text import slugify
from users.models import *
# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название игры")
    image = models.ImageField(upload_to='game_images',default='default.jpg',verbose_name='Картинка игры')
    description = models.TextField(verbose_name="Краткое описание игры",null=True, blank=True)
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата выхода")
    genre = models.CharField(max_length=100, verbose_name="Жанр",null=True, blank=True)
    developer = models.CharField(max_length=100, verbose_name="Разработчик", null=True, blank=True)
    publisher = models.CharField(max_length=100, verbose_name="Издатель", null=True, blank=True)
    platform = models.CharField(max_length=255, verbose_name="Платформа",null=True, blank=True)
    edition = models.CharField(max_length=100, verbose_name="Тип издания",null=True, blank=True)
    os_req = models.CharField(max_length=200, default="0", verbose_name="Операционная система",null=True, blank=True)
    cpu_req = models.CharField(max_length=200, default="0", verbose_name="Процессор",null=True, blank=True)
    ram_req = models.CharField(max_length=200, default="0", verbose_name="Оперативная память",null=True, blank=True)
    gpu_req = models.CharField(max_length=200, default="0", verbose_name="Видеокарта",null=True, blank=True)
    disk_req = models.CharField(max_length=50, default="0", verbose_name="Место на жестком диске",null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, verbose_name="URL-метка")
    screenshots = models.ManyToManyField('Screenshot',blank= True,verbose_name="Скриншоты",related_name='games')
    video_url = models.URLField(blank = True,verbose_name="Ссылка на видео",null=True)

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"

    def __str__(self):
        return self.title

    def save(self,*args ,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Game,self).save(*args,**kwargs)



class Screenshot(models.Model):
    image = models.ImageField( upload_to='screenshots' )
    game = models.ForeignKey(Game,on_delete=models.CASCADE)

    def __str__(self):
        return self.game.title
    class Meta:
        verbose_name = "Скриншот"
        verbose_name_plural = "Скриншоты"


class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)  
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"

    def __str__(self):
        return f"Comment by {self.author} on {self.game}"




