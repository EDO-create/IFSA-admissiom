from django.db import models

# Create your models here.
class Inscription(models.Model):
    FACULTE_CHOICES = [
        ('Sciences Administratives', 'Sciences Administratives'),
        ('Sciences de l\'Éducation', 'Sciences de l\'Éducation'),
    ]

    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    faculte = models.CharField(max_length=100, choices=FACULTE_CHOICES, verbose_name="Faculté choisie")
    
    date_demande = models.DateTimeField(auto_now_add=True, verbose_name="Date de la demande")
    traite = models.BooleanField(default=False, verbose_name="Dossier Traité")

    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.faculte}"

    class Meta:
        verbose_name = "Demande d'Admission"
        verbose_name_plural = "Demandes d'Admission"
        ordering = ['-date_demande']