# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_enseignant_matiereenseignee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enseignant',
            name='matiereEnseignee',
        ),
    ]
