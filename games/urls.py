from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# DRF routers
router = DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'screenshots', ScreenshotViewSet)
router.register(r'comments', CommentViewSet)

# Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="GameBox API",
      default_version='v1',
      description="API для игр, скриншотов и комментариев",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Главные URL
urlpatterns = [
    path('', game_list, name='game_list'),
    path('<int:game_id>/', game_detail , name="game_detail"),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]
