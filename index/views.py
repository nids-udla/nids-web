from typing import Any
from django import http
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_process
from django.contrib.auth import logout as logout_process

class HomeView(View):
    def get(self, request):
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

class TeamView(View):
    def get(self, request):
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

class ProfileView(View):
    def get(self, request):
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

class LoginView(View):
    nav = '''
            <!-- Menu mobil -->
            <div class="flex flex-1 justify-end">
            <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
            <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
            </div>
        '''
    
    def get(self, request):
        return render(request, 'usu-login.html', {
            'opt': self.nav,
        })
    
    def post(self, request):

        print("Llamado correctamente!")

        email = request.POST['email']
        print("1) {}".format(email))
        password = request.POST['password']
        print("2) {}".format(password))
        user = authenticate(username=email, password=password)

        if user:
            login_process(request, user)

            print('autenticado')

            return redirect('/', {
            'opt': self.nav,
        })
        else:
            print('no autenticado')

            return redirect('/', {
            'opt': self.nav,
        })
    
    def logout(self, request):

        logout_process(request)

        return render(request, 'gen-home.html', {
            'opt': self.nav,
        })