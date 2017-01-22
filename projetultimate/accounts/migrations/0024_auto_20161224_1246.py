# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20161224_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='niveau',
        ),
        migrations.AlterField(
            model_name='cours',
            name='idCours',
            field=models.CharField(default=b'COURS', max_length=128, serialize=False, primary_key=True),
        ),
        migrations.AlterUniqueTogether(
            name='cours',
            unique_together=set([('intitule',)]),
        ),
        migrations.RemoveField(
            model_name='cours',
            name='niveau',
        ),
        migrations.DeleteModel(
            name='NiveauClasse',
        ),
    ]
