from django.shortcuts import render
import requests
import os

# Create your views here.
def home(request):
    return render(request, '/general/home.html', {
    })

def team(request):
    return render(request, 'team.html', {
        'team': team.text,
    })