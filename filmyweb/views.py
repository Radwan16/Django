from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Film, DodatkoweInfo, Ocena, Aktor
from .forms import FilmForm, DodatkoweInfoForm, OcenaForm, AktorForm
from django.contrib.auth.decorators import login_required
def wszystkie_filmy(request):
    wszystkie=  Film.objects.all()
    return render(request, 'filmy.html',{'filmy': wszystkie})
@login_required
def nowy_film(request):
    form_film = FilmForm(request.POST or None, request.FILES or None)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None)

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request,'nowy_film.html',{'form':form_film, 'form_dodatkowe':form_dodatkowe, 'nowy':True})
@login_required
def edytuj_film(request,id):
    film = get_object_or_404(Film,pk=id)
    oceny = Ocena.objects.filter(film=film)
    aktorzy = film.aktorzy.all()

    try:
        dodatkowe = DodatkoweInfo.objects.get(film=film.id)
    except DodatkoweInfo.DoesNotExist:
        dodatkowe = None

    form_film = FilmForm(request.POST or None, request.FILES or None, instance=film)
    form_dodatkowe = DodatkoweInfoForm(request.POST or None, instance=dodatkowe)
    form_ocena = OcenaForm(request.POST or None)
    form_aktor = AktorForm(request.POST or None, instance=film)
    if request.method =='POST':
        if 'gwiazdki' in request.POST:
            ocena = form_ocena.save(commit=False)
            ocena.film = film
            ocena.save()
    if request.method =='POST':
        if 'imie' and 'nazwisko' in request.POST:
            aktor = form_aktor.save(commit=False)
            aktor.film = film
            aktor.save()

    if all((form_film.is_valid(), form_dodatkowe.is_valid())):
        film = form_film.save(commit=False)
        dodatkowe = form_dodatkowe.save()
        film.dodatkowe = dodatkowe
        film.save()
        return redirect(wszystkie_filmy)

    return render(request,'nowy_film.html',{'form':form_film, 'form_dodatkowe':form_dodatkowe,'oceny': oceny,'form_ocena':form_ocena,'aktorzy':aktorzy,'form_aktor': form_aktor,'nowy':False})
@login_required
def usun_film(request,id):
    film = get_object_or_404(Film,pk=id)

    if request.method == "POST":
        film.delete()
        return redirect(wszystkie_filmy)

    return render(request,'potwierdz.html',{'film':film})