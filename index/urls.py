from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("team/", views.team, name="team"),
    path("login/", views.login, name="login"),
    path("", include("hero.urls")),
    path("", include("stats.urls")),
    path("", include("news.urls")),
    path("", include("team.urls")),
    path("", include("member.urls")),
]
