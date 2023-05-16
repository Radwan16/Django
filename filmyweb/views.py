from django.shortcuts import render
from django.http import HttpResponse
def test_response(request):
    return HttpResponse("<h1><center>To jest nasz pierwsz test</center></h1>")
