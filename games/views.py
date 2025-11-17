from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def game_list(request):
    query = request.GET.get('q')

    if query:
        games = Game.objects.filter(
            Q(title__icontains = query)|
            Q(genre__icontains = query)|
            Q(developer__icontains = query)|
            Q(publisher__icontains = query)
            )
    else:
        games= Game.objects.all()
        
    context = {
        'games':games
    }
    return render(request,'game_list.html',context)


def game_detail(request,game_id):
    game = get_object_or_404(Game,pk =game_id)

    if request.method =='POST':
        comment_text = request.POST.get('comment')
        if comment_text:
            comment = Comment.objects.create(
                game = game,
                author = request.user,
                content = comment_text,
            )
            request.user.comment_count+=1
            request.user.save()
            messages.success(request,"Успешно добавили коммент")
            return redirect('game_detail',game_id=game.id)
        
    screenshots = game.screenshots.all()
    comments = game.comment_set.all()
    context = {
        'game':game,
        'comments':comments,
        'screenshots':screenshots
    }
    return render(request,'game_detail.html',context)