# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0042_etablissement_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='etablissement',
            name='type_enseignement',
            field=models.CharField(default=1, max_length=128, choices=[(b'GENERAL', b'GENERAL'), (b'TECHNIQUE', b'TECHNIQUE')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='arrondissement',
            field=models.CharField(default=b'Centre', max_length=128, choices=[(b'Centre', ((b'MBANDJOCK', b'BANDJOCKS'), (b'MINTA', b'MINTA'))), (b'Ouest', ((b'MBOUDA', b'MBOUDA'), (b'BATCHAM', b'BATCHAM')))]),
        ),
    ]
