from django.urls import path
from wordle import views as v

urlpatterns = [
    path('getid/', v.api_get_uuid),
    path('getgame/<user>/', v.api_get_game),
    path('guess/<gameid>/<g_uess>/', v.api_guess),
    # path('word/<w>/<freq>/', v.api_addWords),
]