# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminalS', '0004_proposition_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Proposition',
        ),
        migrations.AddField(
            model_name='proposition',
            name='Question',
            field=models.ForeignKey(default='bonjour', to='terminalS.Question'),
            preserve_default=False,
        ),
    ]
