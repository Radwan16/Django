from django.contrib.auth.models import  User
from rest_framework import serializers
from .models import Film,DodatkoweInfo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ['id','tytul','rok','opis','premiera']
class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DodatkoweInfo
        fields = ['id','czas_trwania','gatunek',]