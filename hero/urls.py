from django.urls import path
from . import views

urlpatterns = [
    path("hero/", views.hero, name="hero"),
]