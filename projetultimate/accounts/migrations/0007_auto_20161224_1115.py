# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20161224_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('idNiveau', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(default='test', to='accounts.Niveau'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enseignant',
            name='niveau',
            field=models.ManyToManyField(to='accounts.Niveau'),
        ),
    ]
