from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = ['prenom', 'nom', 'telephone', 'faculte']
        # Pas besoin de widgets ici car on utilise votre HTML personnalisé, 
        # mais le formulaire validera quand même les données.


        