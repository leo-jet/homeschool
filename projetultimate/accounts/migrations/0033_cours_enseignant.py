# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20161226_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='enseignant',
            field=models.ForeignKey(default=1, to='accounts.Enseignant'),
            preserve_default=False,
        ),
    ]
