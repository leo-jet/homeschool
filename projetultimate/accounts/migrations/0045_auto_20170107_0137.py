# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_auto_20170107_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='section',
            field=models.CharField(default=3, max_length=128, choices=[(b'FRANCOPHONE', b'FRANCOPHONE'), (b'ANGLOPHONE', b'ANGLOPHONE'), (b'BILINGUE', b'BILINGUE')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='etablissement',
            name='type_enseignement',
            field=models.CharField(default=2, max_length=128, choices=[(b'GENERAL', b'GENERAL'), (b'TECHNIQUE', b'TECHNIQUE')]),
            preserve_default=False,
        ),
    ]
