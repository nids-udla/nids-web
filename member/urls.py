from django.urls import path, include
from . import views

urlpatterns = [
    path("slogin/", views.slogin, name="slogin"),
]