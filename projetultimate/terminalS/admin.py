from django.contrib import admin

# Register your models here.
from .models import Exercice

class ExerciceAdmin(admin.ModelAdmin):
    class Meta:
        model = Exercice

admin.site.register(Exercice, ExerciceAdmin)