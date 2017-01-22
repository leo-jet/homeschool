# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0048_auto_20170115_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='niveau',
            field=models.ForeignKey(default=2, to='accounts.NiveauClasse'),
            preserve_default=False,
        ),
    ]
