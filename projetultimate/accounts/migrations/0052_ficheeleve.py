# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20170122_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='FicheEleve',
            fields=[
                ('idFiche', models.AutoField(serialize=False, primary_key=True)),
                ('dateReponQuizz', models.DateTimeField(auto_now=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
                ('url', models.CharField(default=b'Test', max_length=128)),
                ('createur', models.ForeignKey(to='accounts.Eleve')),
            ],
        ),
    ]
