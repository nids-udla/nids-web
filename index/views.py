from django.shortcuts import render
import requests
import os

SERVER_DIR = 'http://127.0.0.1:8000/'

# Create your views here.
def home(request):
    hero = requests.get(os.path.join(SERVER_DIR, 'hero'))
    stats = requests.get(os.path.join(SERVER_DIR,'stats'))
    smnews = requests.get(os.path.join(SERVER_DIR,'smnews'))

    return render(request, 'home.html', {
        'hero': hero.text,
        'stats': stats.text,
        'smnews': smnews.text
    })

def team(request):
    team = requests.get(os.path.join(SERVER_DIR, 'steam'))

    return render(request, 'team.html', {
        'team': team.text,
    })

def login(request):
    login = requests.get(os.path.join(SERVER_DIR, 'slogin'))

    return render(request, 'login.html', {
        'login': login.text,
    })