from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def menu(request):
    if request.methode == 'GET':
        return HttpResponse('<h1>welcome</h1>')