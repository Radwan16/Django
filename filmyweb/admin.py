from django.contrib import admin
from .models import Film, DodatkoweInfo

# admin.site.register(Film)
@admin.register(Film)
class Filmadmin(admin.ModelAdmin):
    # fields = ["tytul", "opis", "rok"]
    # exclude = ["opis"]
    list_display = ["tytul", "imdb_rating", "rok"]
    list_filter = ("tytul", "rok")
    search_fields = ("tytul", "opis")

admin.site.register(DodatkoweInfo)