# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_auto_20170104_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='matiereEnseignee',
            field=models.ManyToManyField(to='accounts.Matiere'),
        ),
    ]
