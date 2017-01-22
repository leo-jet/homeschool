# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0036_auto_20161226_1432'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classe',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='classe',
            name='LieuNaissance',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='arrondissement',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='dateNaissance',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='departement',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='lattitude',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='quartier',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='region',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='user',
        ),
    ]
