# Generated by Django 4.1.2 on 2022-10-08 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autosapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name': 'Pais', 'verbose_name_plural': 'Paises'},
        ),
        migrations.AlterModelTable(
            name='pais',
            table='pais',
        ),
    ]
