# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20170107_0137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etablissement',
            name='type_enseignement',
        ),
    ]
