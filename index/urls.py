from django.urls import path, include
from . import views

# ---------------------------------------------------
#
# Teyson:
# /
#
# team/
# profile/<str:name>
#
# news/<int:id>
#
# login/
#
# dashboard/<int:id>
# dashboard/<int:id>/profile
# dashboard/<int:id>/team
# dashboard/<int:id>/projects
# dashboard/<int:id>/projects/tasks
# dashboard/<int:id>/projects/tutorials
#
# ---------------------------------------------------

urlpatterns = [
    path("", views.home, name="home"),
    path("team/", views.team, name="team"),
    path("profile/", views.profile, name="profile"),
    path("login/", views.login, name="login"),
    path("dashboard/<int:id>/profile",views.lgperfil,name='perfil'),
    path("dashboard/<int:id>/myteam", views.myteam, name='myteam'),
    path("dashboard/<int:id>/proyects", views.proyects, name='proyects'),
    path("dashboard/<int:id>/proyects/tasks", views.tasks, name='tasks'),   

    ]
