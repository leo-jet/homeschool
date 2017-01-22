# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_remove_etablissement_type_enseignement'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='type_enseignement',
            field=models.CharField(default=0, max_length=128, choices=[(b'GENERAL', b'GENERAL'), (b'TECHNIQUE', b'TECHNIQUE')]),
            preserve_default=False,
        ),
    ]
