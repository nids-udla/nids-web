from django.shortcuts import redirect, render
from django.views import View
from .login import validate, encrypt, verify
from .models import Usuario
from django.contrib import messages


class HomeView(View):
    nav = ''' 
        <!-- Menu -->
        <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
        <a href="/team" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        <a href="/login/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>

    '''

    def get(self, request):
        return render(request, 'gen-home.html', {
            'opt': self.nav,
        })

class TeamView(View):
    nav = '''
        <!-- Menu mobil -->
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
    '''

    def get(self, request):
        return render(request, 'equ-team.html', {
            'opt': self.nav,
        })

class ProfileView(View):
    nav = '''
        <!-- Menu mobil -->
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
    '''

    def get(self, request):
        return render(request, 'equ-profile.html', {
            'opt': self.nav
        })

# Falta agregar una clase para el detalle de la noticia.

class LoginView(View):
    nav = '''
        <!-- Menu mobil -->
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
    '''
    
    def get(self, request):
        return render(request, 'usu-login.html', {
            'opt': self.nav,
        })
    
    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        checking = validate(email, password)

        if checking is True:
            request.session['is_validated'] = True

            return redirect('/', {
            'opt': self.nav,
        })
        else:
            print('no autenticado')

            return redirect('/login', {
            'opt': self.nav,
        })

class LogoutView(View):

    def post(self, request):
        request.session['is_validated'] = False
        return redirect("home")
    
class RegisterView(View):
    nav = '''
        <!-- Menu mobil -->
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
    '''

    def get(self, request):
        return render(request, 'usu-register.html', {
            'opt': self.nav,
        })
    
    def post(self, request):
        email = request.POST['email']
        is_here = verify(email)

        if is_here is True:
            messages.add_message(request, messages.ERROR, 'Este usuario ya existe!')
            return redirect('register')
        else:
            nombre_completo = request.POST['nombre_completo']
            password = request.POST['password']
            # descripcion = request.POST['descripcion']
            # red_social_A = request.POST['red_social_A']
            # red_social_B = request.POST['red_social_B']
            # red_social_C = request.POST['red_social_C']

            pw = encrypt(password)

            Usuario.objects.create(
                nombre_completo=nombre_completo,
                email=email,
                password=pw,
                # descripcion=descripcion,
                # red_social_A=red_social_A,
                # red_social_B=red_social_B,
                # red_social_C=red_social_C,
                )

            return redirect('/')
