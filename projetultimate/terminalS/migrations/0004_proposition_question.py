# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0003_auto_20161119_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enonce', models.CharField(max_length=128)),
                ('solution', models.CharField(max_length=128)),
                ('point', models.CharField(max_length=128)),
                ('checked', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enonce', models.CharField(max_length=128)),
                ('figure', models.CharField(max_length=128)),
                ('choixMultiple', models.CharField(max_length=128)),
                ('Proposition', models.ForeignKey(to='terminalS.Proposition')),
            ],
        ),
    ]
