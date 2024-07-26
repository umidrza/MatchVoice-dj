from django.urls import path
from .views import *

app_name = 'game'

urlpatterns = [
    path('<int:id>/', match_voice, name='matchvoice'),
    path('<int:id>/gameover/', gameover, name='gameover'),
]
