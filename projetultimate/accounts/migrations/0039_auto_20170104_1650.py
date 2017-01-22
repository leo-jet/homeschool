# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20170104_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercice',
            name='correctionTexte',
            field=models.TextField(default=b'Test2'),
        ),
    ]
