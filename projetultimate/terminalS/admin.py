from django.contrib import admin

# Register your models here.
from .models import Exercice
from .models import Proposition
from .models import Question

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('manuel','chapitre','section','numero','Page','dateCreation','correction','consigneText','correctionTex')
    class Meta:
        model = Exercice
        
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('enonce',
                    'figure',
                    'choixMultiple')
    class Meta:
        model = Question
        
class PropositionAdmin(admin.ModelAdmin):
    list_display = ('enonce',
                    'solution',
                    'point',
                    'checked')
    class Meta:
        model = Proposition

admin.site.register(Exercice, ExerciceAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Proposition, PropositionAdmin) 