# Generated by Django 4.1.3 on 2023-06-05 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_rename_apellido_1_usuario_nombre_completo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario", name="extra_rrss", field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="usuario", name="github", field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name="usuario", name="linkedin", field=models.URLField(blank=True),
        ),
    ]
