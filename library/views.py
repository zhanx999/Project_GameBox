from django.shortcuts import render, redirect
from games.models import Game
from .models import LibraryGame
from django.contrib.auth.decorators import login_required
from django.contrib  import messages
# Create your views here.

@login_required
def remove_from_library(request, game_id):
    game = Game.objects.get(pk=game_id)
    user = request.user

    try :
        library_game = LibraryGame.objects.get(game=game,user=user)
        library_game.delete()
        messages.success(request,"Данная игра удалена из вашей библиотеки!")
    except LibraryGame.DoesNotExist:
        messages.warning(request,"Игра не была в вашей библиотеке!")

    return redirect('user_library')



@login_required
def user_library(request):
    user = request.user
    library_games = LibraryGame.objects.filter(user=user)
    context = {
        'library_games':library_games,
    }
    return render(request,"library/user_library.html",context)



@login_required
def add_to_library(request, game_id):
    game = Game.objects.get(pk=game_id)
    user = request.user

    if request.method =="POST":
        try :
            LibraryGame.objects.get(game=game,user=user)
            messages.warning(request,"Данная игра уже есть в библиотеке")
        except LibraryGame.DoesNotExist:
            LibraryGame.objects.create(game= game,user=user)
            messages.success(request,"Успешно добавили игру!")
        return redirect ('game_detail',game_id=game_id)
    
    context ={
        'game':game,
    }
    return render(request,'library/add_to_library.html',context)
