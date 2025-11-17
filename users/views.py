from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import*
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method =="POST":
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Регистрация прошла успешно")
            return redirect('game_list')
        else:
            messages.error(request,'Пожалуйста,исправьте ошибки ниже.')
    else:
        form = CustomUserCreationForm()
    return render(request,"users/register.html",{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Привет, {username}!')
                return redirect('game_list')
            else:
                messages.error(request, 'Неверные имя пользователя или пароль')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'До свидания.')
    return redirect('game_list')         


@login_required
def profile(request):
    user = request.user

    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST,request.FILES,instance = user)
        if form.is_valid:
            form.save()
            messages.success(request,"Успешно обновились данные!")
            return redirect('profile')
    else:
        form = CustomUserCreationForm(instance = user)
    
    context = {
        'form':form,
        'user':user
    }

    return render(request,"users/profile.html",context)