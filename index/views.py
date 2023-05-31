from django.shortcuts import render
import requests
import os

# Create your views here.
# ---------------------------------------------------
#
# Teyson:
# Crear una def por cada url que lo necesite.
#
# ---------------------------------------------------
def home(request):
    return render(request, 'gen-home.html', {
    })

def team(request):
    return render(request, 'team.html', {
        'team': team.text,
    })