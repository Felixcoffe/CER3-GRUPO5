# Generated by Django 4.1.2 on 2022-12-10 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('SerialNumber', models.IntegerField()),
                ('Propietario', models.CharField(max_length=30)),
                ('Estado', models.CharField(choices=[('En Mantenimeinto', 'En Mantenimiento'), ('Habilitado', 'Habilitado'), ('En Mantenimiento', 'Dado de baja'), ('En Desuso', 'En Desuso'), ('En Prestamo', 'En Prestamo')], max_length=30)),
            ],
        ),
    ]
