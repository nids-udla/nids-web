from django.shortcuts import redirect, render
from django.views import View
from .login import validate, encrypt, verify
from .models import Usuario, Investigacion, Funcion, Rol, Area
from django.contrib import messages


class HomeView(View):
    nav = ''' 
        <!-- Menu -->
        <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
        <a href="/team" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
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
        # Getting the values from the form.
        email = request.POST['email']
        password = request.POST['password']
        # Validating the user.
        checking = validate(email, password)

        if checking is True:
            # Creating the session access.
            request.session['is_validated'] = True
            # Getting the ids needed.
            user = Usuario.objects.get(email=email)

            funcion = Funcion.objects.get(id_usuario=user.id)
            investigacion = Investigacion.objects.get(id_usuario=user.id)

            print('!!!!!! ---> {}'.format(funcion.id_rol))
            print('!!!!!! ---> {}'.format(investigacion))

            rol = Rol.objects.get(id=funcion.id_usuario)
            area = Area.objects.get(id=investigacion.id_area)
            # Saving in session important properties.
            request.session['username'] = user.nombre_completo
            request.session['about'] = user.description
            request.session['rol'] = rol.nombre
            request.session['area'] = area.nombre
            # !!!! ---> Faltan los estudios.
            request.session['socialsA'] = user.linkedin
            request.session['socialsB'] = user.github
            request.session['socialsC'] = user.extra_rrss

            print('!!!!! ---> {}'.format(request.session['socialsA']))
            print('!!!!! ---> {}'.format(request.session['socialsB']))
            print('!!!!! ---> {}'.format(request.session['socialsC']))

            return redirect('dashboard')
        else:
            # Redirecting back to login.
            return redirect('login')

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

class DashboardView(View):

    def get(self, request):
        token = request.session.get('is_validated', False)
        username = request.session.get('username')
        about = request.session.get('about')
        rol = request.session.get('rol')
        area = request.session.get('area')
        # !!!! ---> Faltan los estudios.
        socialsA = request.session.get('socialsA')
        socialsB = request.session.get('socialsB')
        socialsC = request.session.get('socialsC')

        if token == True:           
            return render(request, 'dash-home.html', {
                'username': username,
                'about': about,
                'rol': rol,
                'area': area,
                'socialsA': socialsA,
                'socialsB': socialsB,
                'socialsC': socialsC,
            })
        else:
            return redirect('home')
        
class DashboardProfileView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')

        if token == True:           
            return render(request, 'dash-profile.html', {
                'username': username,
            })
        else:
            return redirect('home')
        
class DashboardProjectView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-proyectos.html', {
                'username': username,
            })
        else:
            return redirect('home')
        
class DashboardProjectTaskView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-tareas.html', {
                'username': username,
            })
        else:
            return redirect('home')

class DashboardTeamView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-team.html', {
                'username': username,
            })
        else:
            return redirect('home')

class DashboardTeamProfileView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-profile.html', {
                'username': username,
            })
        else:
            return redirect('home')
