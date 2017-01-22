# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0050_ficheeleve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficheeleve',
            name='createur',
        ),
        migrations.DeleteModel(
            name='FicheEleve',
        ),
    ]
