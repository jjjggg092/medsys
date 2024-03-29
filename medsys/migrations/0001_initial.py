# Generated by Django 3.0.7 on 2021-06-08 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disposditivo_Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.CharField(max_length=200)),
                ('Modelo', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=200)),
                ('Serie', models.CharField(max_length=200)),
                ('Numero_de_Orden_del_Equipo', models.CharField(max_length=200)),
                ('Estado', models.CharField(max_length=200)),
                ('Fecha_de_Adquisición', models.DateTimeField(verbose_name='date adquisision')),
                ('Fecha_de_Instalación', models.DateTimeField(verbose_name='date instalation')),
                ('Precio_total', models.CharField(max_length=200)),
                ('Observaciones', models.CharField(max_length=200)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
