# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20161224_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='niveau',
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='niveau',
        ),
        migrations.DeleteModel(
            name='Niveau',
        ),
    ]
