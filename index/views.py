from django.shortcuts import redirect, render
from django.views import View
from .login import validate, encrypt, verify,validaremail
from .models import Usuario, Investigacion, Funcion, Rol, Area, Proyecto, Asignado, Tarea, Noticia, Estadisticas
from django.contrib import messages


class HomeView(View):
    nav = ''' 
        <!-- Menu -->
        <a href="#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="#news" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Noticias<span aria-hidden="true"></span></a>
        <a href="/team/" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
    '''

    def get(self, request):
        estadisticas = Estadisticas.objects.all()
        noticias = Noticia.objects.all()

        return render(request, 'gen-home.html', {
            'opt': self.nav,
            'estadisticas': estadisticas,
            'noticias': noticias,
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
        <a href="/team/" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
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

class NewsViews(View):
    nav = ''' 
        <!-- Menu -->
        <a href="/#stats" class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Estadísticas<span aria-hidden="true"></span></a>
        <a href="/team/" target=blank_ class="px-4 text-sm font-semibold leading-6 text-gray-900 hover:text-orange-600">Equipo<span aria-hidden="true"></span></a>
     '''

    def get(self, request, title):
        noticia = Noticia.objects.get(titulo=title)
        noticias = Noticia.objects.all()

        return render(request, 'equ-news.html', {
            'opt': self.nav,
            'noticia': noticia,
            'noticias': noticias,
        })

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
            request.session['email'] = user.email
            request.session['username'] = user.nombre_completo
            request.session['telefono'] = user.telefono            
            request.session['about'] = user.descripcion
            request.session['rol'] = funcion.id_rol.nombre
            request.session['area'] = investigacion.id_area.nombre
            # !!!! ---> Faltan los estudios.
            request.session['linkedin'] = user.linkedin
            request.session['github'] = user.github
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

        data = [
            request.session.get('rol'),
            request.session.get('area'),
            request.session.get('about'),
            request.session.get('email'),
            request.session.get('telefono'),
            request.session.get('linkedin'),
            request.session.get('github'),
        ]

        if token == True:           
            return render(request, 'dash-profile.html', {
                'username': username,
                'rol': data[0],
                'area': data[1],
                'description': data[2],
                'email': data[3],
                'telefono':data[4],
                'linkedin': data[5],
                'github':data[6],
            })
        else:
            return redirect('home')
    def post(self, request):
        if 'email' in request.POST:
            email = request.session.get('email')
            user_email = Usuario.objects.get(email=email)
            gmail = request.POST['email']
            verificar = validaremail(gmail)

            if verificar is True:
                user_email.email = gmail
                user_email.save()
            else:
                return redirect('dashboard')

        if 'telefono' in request.POST:
            numero = request.session.get('telefono')
            user_telefono = Usuario.objects.get(telefono=numero)
            telefono = request.POST['telefono']
            user_telefono.telefono = telefono
            user_telefono.save()

        if 'descripcion' in request.POST:
            description = request.session.get('about')
            user_descripcion = Usuario.objects.get(descripcion=description)
            descripcion = request.POST['descripcion']
            user_descripcion.descripcion = descripcion
            user_descripcion.save()

        if 'linkedin' in request.POST:
            link = request.session.get('linkedin')
            user_link = Usuario.objects.get(linkedin=link)
            linkedin= request.POST['linkedin']
            user_link.linkedin = linkedin
            user_link.save()            

        # Aquí puedes agregar más bloques if para manejar otros formularios

        return redirect('dash-perfil')          

                                         

              
        
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
                'username': username,
                'title': name,
                'tasks': asignaciones,
            })
        else:
            return redirect('home')
        
    def post(self, request, name):
        titulo = request.POST['titulo']

        tarea = Tarea.objects.get(titulo=titulo)
        if tarea.completado is False:
            tarea.completado = True
        else:
            tarea.completado = False
        tarea.save(update_fields=['completado'])

        return redirect ('dash-proyectos')

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

class DashboardAddnewTaskView(View):
    nav = ''' a '''

    def get(self, request, name):
        print('///// ENTRASTE /////')

        token = request.session.get('is_validated', 'False')
        username = request.session.get('username')
        
        if token == True:           
            return render(request, 'dash-addtask.html', {
                'username': username,
            })
        else:
            return redirect('home')
        
    def post(self, request):

        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        fecha_inicio = request.POST['fecha_incio']

    
        return redirect ('dash-añadir-tarea')
