# Generated by Django 4.1.2 on 2022-11-08 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autosapp', '0018_vehiculo_img_alter_empleado_idconcesionario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='categoria',
            field=models.CharField(choices=[('Pesado', 'Pesado'), ('Lijero', 'Ligero'), ('Especial', 'Especiales'), ('Agricola', 'Agricolas'), ('-', '--')], default='-', max_length=15),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='estado',
            field=models.CharField(choices=[('Nuevo', 'Nuevo'), ('Usado', 'Usado'), ('--', '--')], default='-', max_length=6),
        ),
    ]
