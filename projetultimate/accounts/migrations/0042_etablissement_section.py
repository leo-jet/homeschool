# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0041_remove_enseignant_matiereenseignee'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='section',
            field=models.CharField(default=1, max_length=128, choices=[(b'FRANCOPHONE', b'FRANCOPHONE'), (b'ANGLOPHONE', b'ANGLOPHONE'), (b'BILINGUE', b'BILINGUE')]),
            preserve_default=False,
        ),
    ]
