# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0002_exercice_numero'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercice',
            old_name='consigne_text',
            new_name='consigneText',
        ),
        migrations.RenameField(
            model_name='exercice',
            old_name='correction_tex',
            new_name='correctionTex',
        ),
        migrations.RenameField(
            model_name='exercice',
            old_name='date_creation',
            new_name='dateCreation',
        ),
    ]
