from django.shortcuts import render
from django.views import View

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
    def get(self, request):
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