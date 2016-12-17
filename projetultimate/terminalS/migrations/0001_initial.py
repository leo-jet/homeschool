# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('manuel', models.CharField(max_length=128)),
                ('chapitre', models.CharField(max_length=128)),
                ('section', models.CharField(max_length=128)),
                ('Page', models.CharField(max_length=128)),
                ('date_creation', models.DateField()),
                ('correction', models.CharField(max_length=128)),
                ('consigne_text', models.TextField()),
                ('correction_tex', models.TextField()),
            ],
        ),
    ]
