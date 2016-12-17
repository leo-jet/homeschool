# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='numero',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
    ]
