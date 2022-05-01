from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players', views.players, name="players"),
    path('player/<int:id>', views.get_player, name="player")
]

