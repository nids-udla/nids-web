from django.shortcuts import redirect, render
from django.views import View
from .login import validate, encrypt, verify
from .models import Usuario, Investigacion, Funcion, Rol, Area, Proyecto, Asignado, Tarea
from django.contrib import messages


class HomeView(View):
    nav = ''' 
        <!-- Menu -->
        <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
        <a href="/team/" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
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
        users = Usuario.objects.all()
        for e in users:
            funcion = Funcion.objects.get(id_usuario=e.id)
            setattr(e, 'url', '{}'.format(e.nombre_completo))
            setattr(e, 'role', '{}'.format(funcion.id_rol.nombre))
            # Agregar mayor precisión en la selección de la ruta para las fotos.
            setattr(e, 'img', 'img/asistentes/as franco.png')

        return render(request, 'equ-team.html', {
            'opt': self.nav,
            'users': users,
        })

class ProfileView(View):
    nav = '''
        <!-- Menu mobil -->
        <a href="/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Inicio<span aria-hidden="true"></span></a>
        <a href="/team" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
    '''

    def get(self, request, name):
        user = Usuario.objects.get(nombre_completo=name)
        funcion = Funcion.objects.get(id_usuario=user.id)
        setattr(user, 'role', '{}'.format(funcion.id_rol.nombre))
        # Agregar mayor precisión en la selección de la ruta para las fotos.
        setattr(user, 'img', 'img/asistentes/as franco.png')

        return render(request, 'equ-profile.html', {
            'opt': self.nav,
            'user': user,
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
            # Getting the ids needed.
            user = Usuario.objects.get(email=email)
            funcion = Funcion.objects.get(id_usuario=user.id)
            investigacion = Investigacion.objects.get(id_usuario=user.id)
            # Saving in session important properties.
            request.session['username'] = user.nombre_completo
            request.session['about'] = user.descripcion
            request.session['rol'] = funcion.id_rol.nombre
            request.session['area'] = investigacion.id_area.nombre
            # !!!! ---> Faltan los estudios.
            request.session['socialsA'] = user.linkedin
            request.session['socialsB'] = user.github
            # Creating the session access.
            request.session['is_validated'] = True

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

        if token == True:           
            return render(request, 'dash-home.html', {
                'username': username,
            })
        else:
            return redirect('home')
    
class DashboardProfileView(View):
    nav = ''' a '''
    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        rol = request.session.get('rol')
        area = request.session.get('area')

        if token == True:           
            return render(request, 'dash-profile.html', {
                'username': username,
                'rol': rol,
                'area': area,
            })
        else:
            return redirect('home')
        
class DashboardEditProfileView(View):
    nav = ''' a '''    
    def get(self, request):
        token = request.session.get('is_validated', 'False')
        
        if token == True:           
            return render(request, 'dash-edit-profile.html'

            )
        else:
            return redirect('home')
        
    def post(self, request):
        username = request.session.get('username')
        print('///// ---> {}'.format(username))

        user = Usuario.objects.get(nombre_completo=username)
        nombre = request.POST['nombre']
        user.nombre_completo = nombre
        user.save()
        
        print('///// ---> {}'.format(user.nombre_completo))

        return render(request, 'dash-edit-profile.html')
        
class DashboardProjectView(View):
    nav = ''' a '''

    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')

        proyectos = Proyecto.objects.all()
        for e in proyectos:
            setattr(e, 'url', '{}'.format(e.titulo))
        
        if token == True:           
            return render(request, 'dash-proyectos.html', {
                'username': username,
                'projects': proyectos
            })
        else:
            return redirect('home')
        
class DashboardProjectTaskView(View):
    nav = ''' a '''

    def get(self, request, name):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')

        id_proyecto = Proyecto.objects.get(titulo=name)
        asignaciones = Asignado.objects.filter(id_proyecto=id_proyecto)

        for e in asignaciones:
            user = Usuario.objects.get(id=e.id_usuario_id)
            tareas = Tarea.objects.get(id=e.id_tarea_id)
            setattr(e, 'incharge', '{}'.format(user.nombre_completo))
            setattr(e, 'tasktitle', '{}'.format(tareas.titulo))
            setattr(e, 'taskdescription', '{}'.format(tareas.descripcion))
            if tareas.completado:
                setattr(e, 'isdone', 'Completado')
            else:
                setattr(e, 'isdone', 'No completado')

        if token == True:           
            return render(request, 'dash-tareas.html', {
                'title': name,
                'tasks': asignaciones,
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
        
class DashboardprojectTaskcompleteview(View):
    nav = ''' a '''
    def get(self, request):
        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-completar.html', {
                'username': username,
            })
        else:
            return redirect('home')

