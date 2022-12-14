# Generated by Django 4.1.2 on 2022-10-08 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autosapp', '0005_alter_persona_genero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='autosapp.persona')),
                ('idConcesionario', models.CharField(max_length=50)),
                ('paisOrigen', models.CharField(max_length=20)),
            ],
            bases=('autosapp.persona',),
        ),
    ]
