from django.contrib import admin
from django.urls import path
from core.views import start_game

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", start_game, name="start_game"),
]