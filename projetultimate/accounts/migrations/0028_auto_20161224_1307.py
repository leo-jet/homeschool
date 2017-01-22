# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20161224_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapitre',
            name='cours',
        ),
        migrations.RemoveField(
            model_name='college',
            name='etablissement_ptr',
        ),
        migrations.AlterUniqueTogether(
            name='cours',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='cours',
            name='niveau',
        ),
        migrations.AlterUniqueTogether(
            name='eleve',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='eleveinscrita',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='eleveinscrita',
            name='cours',
        ),
        migrations.RemoveField(
            model_name='eleveinscrita',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='eleveinscrita',
            name='etablissement',
        ),
        migrations.AlterUniqueTogether(
            name='enseignant',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='niveau',
        ),
        migrations.RemoveField(
            model_name='enseignant',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='enseignea',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='enseignea',
            name='enseignant',
        ),
        migrations.RemoveField(
            model_name='enseignea',
            name='etablissement',
        ),
        migrations.DeleteModel(
            name='Exercice',
        ),
        migrations.RemoveField(
            model_name='lycee',
            name='etablissement_ptr',
        ),
        migrations.DeleteModel(
            name='NiveauClasse',
        ),
        migrations.DeleteModel(
            name='Proposition',
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='question',
            name='propositions',
        ),
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.AlterUniqueTogether(
            name='quizz',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='enseignant',
        ),
        migrations.RemoveField(
            model_name='quizz',
            name='question',
        ),
        migrations.AlterUniqueTogether(
            name='reponda',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='reponda',
            name='eleve',
        ),
        migrations.RemoveField(
            model_name='reponda',
            name='quizz',
        ),
        migrations.RemoveField(
            model_name='section',
            name='chapitre',
        ),
        migrations.RemoveField(
            model_name='universite',
            name='etablissement_ptr',
        ),
        migrations.DeleteModel(
            name='Chapitre',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='Cours',
        ),
        migrations.DeleteModel(
            name='Eleve',
        ),
        migrations.DeleteModel(
            name='EleveInscritA',
        ),
        migrations.DeleteModel(
            name='Enseignant',
        ),
        migrations.DeleteModel(
            name='EnseigneA',
        ),
        migrations.DeleteModel(
            name='Etablissement',
        ),
        migrations.DeleteModel(
            name='Lycee',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Quizz',
        ),
        migrations.DeleteModel(
            name='RepondA',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Universite',
        ),
    ]
