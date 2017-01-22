# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0034_auto_20161226_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('dateNaissance', models.DateField()),
                ('LieuNaissance', models.CharField(default=b'Test', max_length=128)),
                ('region', models.CharField(default=b'Test', max_length=128)),
                ('departement', models.CharField(default=b'Test', max_length=128)),
                ('arrondissement', models.CharField(default=b'Test', max_length=128)),
                ('quartier', models.CharField(default=b'Test', max_length=128)),
                ('longitude', models.CharField(default=b'Test', max_length=128)),
                ('lattitude', models.CharField(default=b'Test', max_length=128)),
                ('idClass', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('eleves', models.ManyToManyField(to='accounts.Eleve')),
                ('enseignant', models.ForeignKey(to='accounts.Enseignant')),
                ('niveau', models.ForeignKey(to='accounts.NiveauClasse')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='classe',
            unique_together=set([('user', 'dateNaissance')]),
        ),
    ]
