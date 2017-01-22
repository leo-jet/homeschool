# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161224_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('idNiveau', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(default=datetime.datetime(2016, 12, 24, 11, 8, 19, 543889, tzinfo=utc), to='accounts.Niveau'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enseignant',
            name='niveau',
            field=models.ManyToManyField(to='accounts.Niveau'),
        ),
    ]
