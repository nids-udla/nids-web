# Generated by Django 4.1.3 on 2023-07-07 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="usuario", name="extra_rrss",),
        migrations.AddField(
            model_name="tarea",
            name="completado",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="tarea",
            name="fecha_inicio",
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name="usuario",
            name="telefono",
            field=models.CharField(default="none", max_length=300),
        ),
    ]