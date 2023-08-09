from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul','rok','premiera','opis','imdb_rating','plakat']