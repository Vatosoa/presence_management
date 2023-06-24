from django.contrib import admin
from .models import Administrateur, Enseignant, Etudiant, Salle
from .models import Module, Examen, Groupe, Section, Presence, Surveillant
# Register your models here.

class SalleAdmin(admin.ModelAdmin):
    exclude = ('id_salle',)  # Exclure le champ id_salle lors de l'édition


class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id_exam', 'salle', 'get_nom_module', 'start_time', 'end_time')

    def get_nom_module(self, obj):
        if obj.enseignant and obj.enseignant.module:
            return obj.enseignant.module.nom_module
        return ''
    get_nom_module.short_description = 'Nom du module'

admin.site.register(Examen, ExamenAdmin)

admin.site.register(Administrateur)
admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(Salle, SalleAdmin)
admin.site.register(Module)
admin.site.register(Groupe)
admin.site.register(Section)
admin.site.register(Surveillant)
admin.site.register(Presence)