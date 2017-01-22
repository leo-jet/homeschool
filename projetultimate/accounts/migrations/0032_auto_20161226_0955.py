# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20161224_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitre',
            name='niveau',
            field=models.ForeignKey(default=1, to='accounts.NiveauClasse'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='cours',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='cours',
            name='niveau',
        ),
    ]
