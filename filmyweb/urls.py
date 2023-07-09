from django.urls import path
from filmyweb.views import wszystkie_filmy,nowy_film

urlpatterns = [
    path('wszystkie/',wszystkie_filmy),
    path('nowy/',nowy_film),
]