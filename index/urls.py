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
    ]
