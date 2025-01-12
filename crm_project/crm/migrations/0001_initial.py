# Generated by Django 5.0.7 on 2024-07-23 17:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='EjecutivoCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contacto')),
                ('ejecutivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ejecutivocuenta')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('estado', models.CharField(choices=[('Cliente Potencial', 'Cliente Potencial'), ('Propuesta en Curso', 'Propuesta en Curso'), ('Cliente Potencial Asegurado', 'Cliente Potencial Asegurado'), ('Propuesta Enviada', 'Propuesta Enviada'), ('Cerrado', 'Cerrado')], max_length=50)),
                ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.contacto')),
                ('ejecutivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.ejecutivocuenta')),
            ],
        ),
        migrations.CreateModel(
            name='OportunidadVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_cierre', models.DateField()),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.lead')),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('asignado_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.proyecto')),
            ],
        ),
    ]
