# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0007_auto_20161219_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposition',
            name='Question',
        ),
        migrations.DeleteModel(
            name='Proposition',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
