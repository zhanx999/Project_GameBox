from django.urls import path
from .views import *


urlpatterns = [
    path('<int:game_id>/add_to_library/',add_to_library,name ="add_to_library"),
    path('',user_library,name="user_library"),
    path('<int:game_id>/remove_from_library/',remove_from_library,name ="remove_from_library"),
]

