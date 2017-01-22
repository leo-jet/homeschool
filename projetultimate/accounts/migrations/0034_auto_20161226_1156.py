# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_cours_enseignant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cours',
            name='enseignant',
        ),
        migrations.AddField(
            model_name='cours',
            name='enseignant',
            field=models.ManyToManyField(to='accounts.Enseignant'),
        ),
    ]
