# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_etablissement_type_enseignement'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercice',
            name='publier',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='region',
            field=models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'ExtremeNord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')]),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='region',
            field=models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'ExtremeNord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')]),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='region',
            field=models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'ExtremeNord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')]),
        ),
    ]
