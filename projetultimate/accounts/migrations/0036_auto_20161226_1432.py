# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0035_auto_20161226_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupeDeSoutien',
            fields=[
                ('etablissement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='accounts.Etablissement')),
                ('idGroupeDeSoutien', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
            ],
            bases=('accounts.etablissement',),
        ),
        migrations.AddField(
            model_name='classe',
            name='etablissement',
            field=models.ForeignKey(default=1, to='accounts.Etablissement'),
            preserve_default=False,
        ),
    ]
