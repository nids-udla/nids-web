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
from .views import HomeView, TeamView, ProfileView, LoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team/', TeamView.as_view(), name='team'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
]
