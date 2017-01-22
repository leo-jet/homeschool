# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0013_auto_20161219_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('departement', models.CharField(max_length=128)),
                ('arrondissement', models.CharField(max_length=128)),
                ('quartier', models.CharField(max_length=128)),
                ('longitude', models.CharField(max_length=128)),
                ('lattitude', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=128)),
                ('prenom', models.CharField(max_length=128)),
                ('dateNaissance', models.DateField()),
                ('LieuNaissance', models.CharField(max_length=128)),
                ('region', models.CharField(max_length=128)),
                ('departement', models.CharField(max_length=128)),
                ('arrondissement', models.CharField(max_length=128)),
                ('quartier', models.CharField(max_length=128)),
                ('longitude', models.CharField(max_length=128)),
                ('lattitude', models.CharField(max_length=128)),
            ],
        ),
    ]
