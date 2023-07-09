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

from django.urls import path
from .views import HomeView, TeamView, ProfileView, LoginView, LogoutView, RegisterView, DashboardView, DashboardProfileView, DashboardProjectView, DashboardProjectTaskView, DashboardTeamView, DashboardTeamProfileView, DashboardEditProfileView, DashboardprojectTaskcompleteview

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team/', TeamView.as_view(), name='team'),
    path('team/<str:name>', ProfileView.as_view(), name='profile'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/perfil', DashboardProfileView.as_view(), name='dash-perfil'),
    path('dashboard/perfil/edit/', DashboardEditProfileView.as_view(), name='dash-perfil-edit'),
    path('dashboard/proyectos', DashboardProjectView.as_view(), name='dash-proyectos'),
    path('dashboard/proyectos/tareas/<str:name>', DashboardProjectTaskView.as_view(), name='dash-proyectos-tareas'),
    # path('dashboard/proyectos/tareas/completar', DashboardprojectTaskcompleteview.as_view(), name='dash-tareas-completar'),
    path('dashboard/equipo', DashboardTeamView.as_view(), name='dash-equipo'),
    path('dashboard/equipo/profile', DashboardTeamProfileView.as_view(), name='dash-compañero'),
]