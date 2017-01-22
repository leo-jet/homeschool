# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0010_auto_20161219_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enonce', models.CharField(max_length=128)),
                ('solution', models.CharField(max_length=128)),
                ('point', models.CharField(max_length=128)),
                ('checked', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enonce', models.CharField(max_length=128)),
                ('figure', models.CharField(max_length=128)),
                ('choixMultiple', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='proposition',
            name='Question',
            field=models.ForeignKey(to='terminalS.Question'),
        ),
    ]
