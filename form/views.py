from django.shortcuts import render, redirect
from django.contrib import messages
from .form import InscriptionForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        # On remplit le formulaire avec les données reçues (POST)
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save() # Sauvegarde dans la base de données
            # Message de succès qui s'affichera dans le bloc vert ajouté au HTML
            messages.success(request, "Votre demande a été envoyée avec succès ! L'administration vous contactera sous peu.")
            return redirect('home') # Redirige vers la même page pour éviter le renvoi du formulaire
        else:
            messages.error(request, "Une erreur est survenue. Vérifiez vos informations.")
    
    return render(request, 'index.html')