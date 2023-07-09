from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['Tytul','opis','premiera','rok','imdb_rating','plakat']
