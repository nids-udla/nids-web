from django.shortcuts import render
from .models import Proyecto,Tarea,Funcion,Usuario,Noticia

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
})

def team(request):
    return render(request, 'not-team.html', {
        'team': team.text,
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
def news(request):
    news:Noticia.objects.all()
    return render(request, "equ-news.html",{
        'noticias':news
    })

def profile(request):
    profile=Usuario.objects.all()
    return render(request, 'equ-profile.html',{
        "profile": profile 
    })
def lgperfil(request):
    lgperfil=Usuario.objects.all()
    return render(request, 'usu-perfil.html',{
        "perfil": lgperfil
    })
def myteam(request):
    myteam=Funcion.objects.all()
    return render(request, 'usu-myteam.html',{
        "myteam": myteam
    })
def proyects(request):
    proyects=Proyecto.objects.all()
    return render(request, 'usu-proyects.html',{
        'proyectos': proyects
    })
def tasks(request):
    tasks=Tarea.objects.all()
    return render(request, 'usu-tareas.html', {
        'tareas': tasks
    })