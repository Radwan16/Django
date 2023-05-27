from django.urls import path
from filmyweb.views import wszystkie_filmy

urlpatterns = [
    path('wszystkie/',wszystkie_filmy)
]