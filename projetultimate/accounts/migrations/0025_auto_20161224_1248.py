# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20161224_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='NiveauClasse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'Terminale C', max_length=128, choices=[(b'Enseignement G\xc3\xa9nerale', ((b'Terminale A', b'Terminale A'), (b'Terminale A', b'Terminale B'), (b'Terminale C', b'Terminale C'), (b'Terminale D', b'Terminale D'), (b'Terminale E', b'Terminale E')))])),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='niveauclasse',
            unique_together=set([('intitule',)]),
        ),
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(default=1, to='accounts.NiveauClasse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enseignant',
            name='niveau',
            field=models.ManyToManyField(to='accounts.NiveauClasse'),
        ),
    ]
