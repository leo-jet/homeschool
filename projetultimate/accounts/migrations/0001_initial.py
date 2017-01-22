# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('idChapitre', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('idCours', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'MATHEMATIQUES', max_length=128, choices=[(b'MATHEMATIQUES', b'MATHEMATIQUES'), (b'PHYSIQUES', b'PHYSIQUES'), (b'CHIMIE', b'CHIMIE'), (b'SCIENCE DE LA VIE ET DE LA TERRE', b'SCIENCE DE LA VIE ET DE LA TERRE')])),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('dateNaissance', models.DateField()),
                ('LieuNaissance', models.CharField(default=b'Test', max_length=128)),
                ('region', models.CharField(default=b'Test', max_length=128)),
                ('departement', models.CharField(default=b'Test', max_length=128)),
                ('arrondissement', models.CharField(default=b'Test', max_length=128)),
                ('quartier', models.CharField(default=b'Test', max_length=128)),
                ('longitude', models.CharField(default=b'Test', max_length=128)),
                ('lattitude', models.CharField(default=b'Test', max_length=128)),
                ('idEleve', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EleveInscritA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annee', models.DateField()),
                ('cours', models.ForeignKey(to='accounts.Cours')),
                ('eleve', models.ForeignKey(to='accounts.Eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('dateNaissance', models.DateField()),
                ('LieuNaissance', models.CharField(default=b'Test', max_length=128)),
                ('region', models.CharField(default=b'Test', max_length=128)),
                ('departement', models.CharField(default=b'Test', max_length=128)),
                ('arrondissement', models.CharField(default=b'Test', max_length=128)),
                ('quartier', models.CharField(default=b'Test', max_length=128)),
                ('longitude', models.CharField(default=b'Test', max_length=128)),
                ('lattitude', models.CharField(default=b'Test', max_length=128)),
                ('idEnseignant', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('specialite', models.CharField(default=b'Test', max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EnseigneA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annee', models.DateField()),
                ('enseignant', models.ForeignKey(to='accounts.Enseignant')),
            ],
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(default=b'Test', max_length=128)),
                ('region', models.CharField(default=b'Adamaoua', max_length=128, choices=[(b'Adamaoua', b'Adamaoua'), (b'Centre', b'Centre'), (b'Est ', b'Est'), (b'Extr\xc3\xaame-Nord ', b'Extr\xc3\xaame-Nord'), (b'Littoral', b'Littoral'), (b'Nord', b'Nord'), (b'Nord-Ouest ', b'Nord-Ouest'), (b'Ouest', b'Ouest'), (b'Sud', b'Sud'), (b'Sud-Ouest', b'Sud-Ouest')])),
                ('departement', models.CharField(default=b'Test', max_length=128)),
                ('arrondissement', models.CharField(max_length=128, choices=[(b'Centre', ((b'MBANDJOCK', b'BANDJOCKS'), (b'MINTA', b'MINTA'))), (b'Ouest', ((b'MBOUDA', b'MBOUDA'), (b'BATCHAM', b'BATCHAM')))])),
                ('quartier', models.CharField(default=b'Test', max_length=128)),
                ('longitude', models.CharField(default=b'Test', max_length=128)),
                ('lattitude', models.CharField(default=b'Test', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Exercice',
            fields=[
                ('idExercice', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('manuel', models.CharField(max_length=128)),
                ('chapitre', models.CharField(max_length=128)),
                ('section', models.CharField(max_length=128)),
                ('numero', models.CharField(max_length=8)),
                ('Page', models.CharField(max_length=128)),
                ('dateCreation', models.DateField()),
                ('correction', models.CharField(max_length=128)),
                ('consigneText', models.TextField()),
                ('correctionTex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('idProposition', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('enonce', models.CharField(default=b'Test', max_length=128)),
                ('solution', models.CharField(default=b'Test', max_length=128)),
                ('point', models.DecimalField(max_digits=3, decimal_places=2)),
                ('checked', models.CharField(default=b'Test', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('idQuestion', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('enonce', models.CharField(default=b'Test', max_length=128)),
                ('figure', models.CharField(default=b'Test', max_length=128)),
                ('choixMultiple', models.CharField(default=b'Test', max_length=128)),
                ('propositions', models.ManyToManyField(to='accounts.Proposition')),
            ],
        ),
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('idQuizz', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('dateCreationQuizz', models.DateTimeField(auto_now=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
                ('eleve', models.ManyToManyField(to='accounts.Eleve')),
                ('enseignant', models.ForeignKey(to='accounts.Enseignant')),
                ('question', models.ManyToManyField(to='accounts.Question')),
            ],
        ),
        migrations.CreateModel(
            name='RepondA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.DecimalField(max_digits=2, decimal_places=1)),
                ('dateReponQuizz', models.DateTimeField(auto_now=True)),
                ('eleve', models.ForeignKey(to='accounts.Eleve')),
                ('quizz', models.ForeignKey(to='accounts.Quizz')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('idSection', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('intitule', models.CharField(default=b'Test', max_length=128)),
                ('chapitre', models.ForeignKey(to='accounts.Chapitre')),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('etablissement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='accounts.Etablissement')),
                ('idCollege', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('directeur', models.CharField(default=b'Test', max_length=128)),
            ],
            bases=('accounts.etablissement',),
        ),
        migrations.CreateModel(
            name='Lycee',
            fields=[
                ('etablissement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='accounts.Etablissement')),
                ('idLycee', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('principal', models.CharField(default=b'Test', max_length=128)),
            ],
            bases=('accounts.etablissement',),
        ),
        migrations.CreateModel(
            name='Universite',
            fields=[
                ('etablissement_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='accounts.Etablissement')),
                ('idLycee', models.CharField(default=b'Test', max_length=128, serialize=False, primary_key=True)),
                ('recteur', models.CharField(default=b'Test', max_length=128)),
            ],
            bases=('accounts.etablissement',),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.ForeignKey(to='accounts.Section'),
        ),
        migrations.AlterUniqueTogether(
            name='proposition',
            unique_together=set([('enonce',)]),
        ),
        migrations.AddField(
            model_name='enseignea',
            name='etablissement',
            field=models.ForeignKey(to='accounts.Etablissement'),
        ),
        migrations.AddField(
            model_name='eleveinscrita',
            name='etablissement',
            field=models.ForeignKey(to='accounts.Etablissement'),
        ),
        migrations.AddField(
            model_name='chapitre',
            name='cours',
            field=models.ForeignKey(to='accounts.Cours'),
        ),
        migrations.AlterUniqueTogether(
            name='reponda',
            unique_together=set([('dateReponQuizz', 'quizz')]),
        ),
        migrations.AlterUniqueTogether(
            name='quizz',
            unique_together=set([('dateCreationQuizz', 'intitule')]),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('enonce',)]),
        ),
        migrations.AlterUniqueTogether(
            name='enseignea',
            unique_together=set([('annee', 'etablissement', 'enseignant')]),
        ),
        migrations.AlterUniqueTogether(
            name='enseignant',
            unique_together=set([('user', 'dateNaissance')]),
        ),
        migrations.AlterUniqueTogether(
            name='eleveinscrita',
            unique_together=set([('etablissement', 'eleve', 'cours', 'annee')]),
        ),
        migrations.AlterUniqueTogether(
            name='eleve',
            unique_together=set([('user', 'dateNaissance')]),
        ),
    ]
