# Generated by Django 4.2 on 2023-05-11 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barbero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('dni', models.CharField(max_length=32)),
                ('especialidad', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('dni', models.CharField(max_length=32)),
                ('telefono', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=64)),
                ('duracion_minutos', models.IntegerField()),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_turno', models.DateField()),
                ('hora_turno', models.TimeField()),
                ('barbero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPreentrega.barbero')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPreentrega.cliente')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppPreentrega.servicio')),
            ],
        ),
    ]
