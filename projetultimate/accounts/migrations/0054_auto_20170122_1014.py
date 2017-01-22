# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0053_auto_20170122_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficheeleve',
            old_name='dateReponQuizz',
            new_name='dateCreation',
        ),
    ]
