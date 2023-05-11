from django.urls import path
from . import views

urlpatterns = [
    path("smnews/", views.smnews, name="smnews"),
]