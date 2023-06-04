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
    nav = ''' 
            <!-- Menu -->
            <div class="flex flex-1 justify-end">
            <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
            <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
            <a href="/team" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
            <a href="/login" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
            </div>
        '''
    return render(request, 'gen-home.html', {
        'opt': nav,
    })

def team(request):
    nav = '''
            <!-- Menu mobil -->
            <div class="flex flex-1 justify-end">
            <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
            <a href="/login" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
            </div>
        '''
    return render(request, 'equ-team.html', {
        'currenturl': 'team',
        'opt': nav,
    })

def profile(request):
    nav = '''
        <!-- Menu mobil -->
        <div class="flex flex-1 justify-end">
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        <a href="/login" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
        </div>
    '''
    return render(request, 'equ-profile.html', {
        'opt': nav
    })

def login(request):
    nav = '''
        <!-- Menu mobil -->
        <div class="flex flex-1 justify-end">
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        </div>
    '''
    return render(request, 'usu-login.html', {
        'opt': nav,
    })