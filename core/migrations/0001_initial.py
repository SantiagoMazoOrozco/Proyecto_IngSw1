# Generated by Django 5.2.3 on 2025-06-12 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emulador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('archivo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('nickname', models.CharField(max_length=50, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('archivo_rom', models.CharField(max_length=255)),
                ('imagen_portada', models.CharField(blank=True, max_length=255, null=True)),
                ('emulador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.emulador')),
                ('plataforma', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.plataforma')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
                ('ultima_conexion', models.DateTimeField(auto_now=True)),
                ('juego_favorito', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perfiles_favoritos', to='core.game')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='JuegoJugado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo_jugado', models.IntegerField(default=0)),
                ('ultima_vez', models.DateTimeField(auto_now=True)),
                ('logros', models.TextField(blank=True, null=True)),
                ('archivo_guardado', models.CharField(blank=True, max_length=255, null=True)),
                ('clip', models.CharField(blank=True, max_length=255, null=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.game')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Estadisticas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_tiempo_jugado', models.IntegerField(default=0)),
                ('juego_mas_jugado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estadisticas_mas_jugado', to='core.game')),
                ('ultimo_juego', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='estadisticas_ultimo_juego', to='core.game')),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.perfil')),
            ],
        ),
    ]
