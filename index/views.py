from django.shortcuts import redirect, render
from django.views import View
from .login import verify, encrypt
from .models import Usuario

class HomeView(View):
    nav = ''' 
        <!-- Menu -->
        <div class="flex flex-1 justify-end">
        <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
        <a href="/team" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        <a href="/login/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
        </div>
    '''

    def get(self, request):
        return render(request, 'gen-home.html', {
            'opt': self.nav,
        })

class TeamView(View):
    nav = '''
        <!-- Menu mobil -->
        <div class="flex flex-1 justify-end">
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/login/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
        </div>
    '''

    def get(self, request):
        return render(request, 'equ-team.html', {
            'opt': self.nav,
        })

class ProfileView(View):
    nav = '''
        <!-- Menu mobil -->
        <div class="flex flex-1 justify-end">
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        <a href="/login/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
        </div>
    '''

    def get(self, request):
        return render(request, 'equ-profile.html', {
            'opt': self.nav
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
        password = request.POST['password']
        checking = verify(email=email, password=password)

        print("1) {}".format(email))
        print("2) {}".format(password))

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
    
class RegisterView(View):
    nav = '''
        <!-- Menu mobil -->
        <div class="flex flex-1 justify-end">
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
        <a href="/login/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Log In<span aria-hidden="true"></span></a>
        </div>
    '''

    def get(self, request):
        return render(request, 'usu-register.html', {
            'opt': self.nav,
        })
    
    def post(self, request):
        nombre_completo = request.POST['nombre_completo']
        email = request.POST['email']
        password = request.POST['password']
        descripcion = request.POST['descripcion']
        red_social_A = request.POST['red_social_A']
        red_social_B = request.POST['red_social_B']
        red_social_C = request.POST['red_social_C']

        pw = encrypt(password)

        newUser = Usuario.objects.create(
            nombre_completo=nombre_completo,
            email=email,
            password=pw,
            descripcion=descripcion,
            red_social_A=red_social_A,
            red_social_B=red_social_B,
            red_social_C=red_social_C,
            )

        return render(request, 'home.html')