from django.urls import path
from .views import *

urlpatterns = [
    path('', game_list,name='game_list'),
    path('<int:game_id>/',game_detail , name ="game_detail")
]
