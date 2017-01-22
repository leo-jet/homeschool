# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20161224_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='NiveauClasse',
            fields=[
                ('intitule', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(to='accounts.NiveauClasse'),
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='niveau',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='niveau',
            field=models.ManyToManyField(to='accounts.NiveauClasse'),
        ),
    ]
