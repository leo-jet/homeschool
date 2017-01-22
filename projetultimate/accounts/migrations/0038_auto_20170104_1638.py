# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20161226_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'MATHEMATIQUES', max_length=128, choices=[(b'MATHEMATIQUES', b'MATHEMATIQUES'), (b'PHYSIQUES', b'PHYSIQUES'), (b'CHIMIE', b'CHIMIE'), (b'SCIENCE DE LA VIE ET DE LA TERRE', b'SCIENCE DE LA VIE ET DE LA TERRE')])),
            ],
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='Page',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='chapitre',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='consigneText',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='correctionTex',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='manuel',
        ),
        migrations.RemoveField(
            model_name='exercice',
            name='numero',
        ),
        migrations.AddField(
            model_name='exercice',
            name='consigneTexte',
            field=models.TextField(default=b'Test'),
        ),
        migrations.AddField(
            model_name='exercice',
            name='correctionTexte',
            field=models.TextField(default=b'Test'),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='arrondissement',
            field=models.CharField(max_length=128, choices=[(b'Centre', ((b'MBANDJOCK', b'BANDJOCKS'), (b'MINTA', b'MINTA'))), (b'Ouest', ((b'MBOUDA', b'MBOUDA'), (b'BATCHAM', b'BATCHAM')))]),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='region',
            field=models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'Extr\xc3\xaame-Nord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest ', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')]),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='arrondissement',
            field=models.CharField(max_length=128, choices=[(b'Centre', ((b'MBANDJOCK', b'BANDJOCKS'), (b'MINTA', b'MINTA'))), (b'Ouest', ((b'MBOUDA', b'MBOUDA'), (b'BATCHAM', b'BATCHAM')))]),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='region',
            field=models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'Extr\xc3\xaame-Nord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest ', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')]),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='correction',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='dateCreation',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='exercice',
            name='section',
            field=models.ForeignKey(to='accounts.Section'),
        ),
        migrations.AlterUniqueTogether(
            name='matiere',
            unique_together=set([('intitule',)]),
        ),
    ]
