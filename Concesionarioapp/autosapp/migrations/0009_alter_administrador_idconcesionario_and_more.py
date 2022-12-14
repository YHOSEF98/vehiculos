# Generated by Django 4.1.2 on 2022-10-08 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autosapp', '0008_alter_administrador_paisorigen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='idConcesionario',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='paisOrigen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='autosapp.pais'),
        ),
    ]
