from django.db import models

# Create your models here.
# ---------------------------------------------------
#
# Matias:
# Crear models de la base de datos.
# https://lucid.app/lucidchart/67ceb36c-9d7e-43df-86d4-9431dc54e118/edit?page=0_0&invitationId=inv_72a258e6-641b-4c3b-aa6e-cbf3c75ca1dc#
#
# ---------------------------------------------------
class usuario(models.Model):
    nombre1 = models.CharField(max_length=25, default="none")
    nombre2 = models.CharField(max_length=25, default="none")
    apellido1 = models.CharField(max_length=25, default="none")
    apellido2 = models.CharField(max_length=25, default="none")
    descripcion = models.CharField(max_length=75, default="none")
    Linkedin = models.URLField(max_length=200, default="none")
    github = models.URLField(max_length=200, default="none")
    rrss_extra = models.URLField(max_length=200, default="none")
    codigo = models.CharField(max_length=8, default="none")

class rol(models.Model):
    nombre = models.CharField(max_length=25, default="none")

#foreignkey rol-usuario
class funcion(models.model):
    id_rol = models.ForeignKey(rol, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class area(models.Model):
    nombre = models.CharField(max_length=25, default="none")

class investigacion(models.Model):
    id_area = models.ForeignKey(area, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class diploma(models.Model):
    nombre = models.CharField(max_length=25, default="none")
    tipo = models.CharField(max_length=25, default="none")

#foreignkey area - investigacion
class graduado(models.Model):
    id_diploma = models.ForeignKey(diploma, default="none")
    id_usuario = models.ForeignKey(usuario, default="none")

#---------------------------------------En duda------------------------------------------------------
class noticia(models.Model):
    titulo = models.CharField(max_length=25, default="none")
    palabra_clave = models.CharField(max_length=100, default="none")
    descripcion = models.CharField(max_length=300, default="none")
    id_autor = models.ForeignKey(autor, default="none")

class autor(models.Model):
    id_usuario = models.ForeignKey(usuario, default="none")
    id_noticia = models.ForeignKey(noticia, default="none") 

#---------------------------------------En duda-------------------------------------------------------

class proyecto(models.Model):
    titulo = models.CharField(max_length=25, default="none")
    descripcion = models.CharField(max_length=50, default="none") 

class tarea(models.Model):
    titulo = models.CharField(max_length=25, default="none")
    descripcion = models.CharField(max_length=50, default="none") 

#foreignkey proyecto - tarea
class asignado(models.Model):
    id_proyecto = models.ForeignKey(proyecto, default="none")
    id_tarea = models.ForeignKey(tarea, default="none")
    id_usuario = models.ForeignKey(usuario, default="none")

class estadistica(models.Model):
    titulo = models.CharField(max_length=25, default="none")
    valor = models.IntegerField()
