from django.contrib import admin
from .models import Inscription

# Register your models here.

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'telephone', 'faculte', 'date_demande', 'traite')
    list_filter = ('faculte', 'traite', 'date_demande')
    search_fields = ('nom', 'prenom', 'telephone')
    list_editable = ('traite',) # Permet de cocher "Traité" directement dans la liste