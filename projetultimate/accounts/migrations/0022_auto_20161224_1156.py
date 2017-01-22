# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20161224_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='niveau',
            field=models.CharField(default=b'Test', max_length=128),
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='niveau',
        ),
        migrations.AddField(
            model_name='enseignant',
            name='niveau',
            field=models.CharField(default=b'Test', max_length=128),
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
    ]
