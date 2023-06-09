from django.db import models

# -------------------------------------------
# Independent Classes:
#   Estadisticas
#   Tarea
#   Rol
#   Diploma
#   Area
#   Proyecto
#
# Dependent Classes:
#   Usuario
#   Autor
#   Noticia
#   Investigacion
#   Funcion
#   Graduado
#   Asignado
# -------------------------------------------
class Usuario(models.Model):
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, default="none") # Editable
    password = models.CharField(max_length=300) # Editable solo por profesores
    telefono = models.CharField(max_length=300, default="none") # Editable
    descripcion = models.CharField(max_length=100) # Editable
    linkedin = models.URLField(blank=True) # Editable
    github = models.URLField(blank=True) # Editable
    
class Estadisticas(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)
    fecha_inicio = models.DateField(default=None)

class Rol(models.Model):
    nombre = models.CharField(max_length=100)

class Diploma(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

class Area(models.Model):
    nombre = models.CharField(max_length=100)

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    palabra_clave = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    fecha_inicio = models.DateField(default=None)

# -------------------------------------------

class Autor(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_noticia = models.ForeignKey('Noticia', on_delete=models.CASCADE)

class Investigacion(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_area = models.ForeignKey('Area', on_delete=models.CASCADE)

class Funcion(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_rol = models.ForeignKey('Rol', on_delete=models.CASCADE)

class Graduado(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_diploma = models.ForeignKey('Diploma', on_delete=models.CASCADE)

class Asignado(models.Model):
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)
    id_tarea = models.ForeignKey('Tarea', on_delete=models.CASCADE)