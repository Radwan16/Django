from django.shortcuts import render
from django.http import HttpResponse
def wszystkie_filmy(request):
    # return HttpResponse("<h1><center>To jest nasz pierwsz test</center></h1>")
    return render(request, 'filmy.html')
