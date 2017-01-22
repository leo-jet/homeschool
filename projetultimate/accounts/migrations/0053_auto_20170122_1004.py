# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_ficheeleve'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ficheeleve',
            unique_together=set([('url',)]),
        ),
    ]
