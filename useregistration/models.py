from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

#from django.contrib.auth.models import User

User = get_user_model()


class Administrateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    id_user = models.IntegerField()
    nom_admin = models.CharField(max_length=50)
    prenom_admin = models.CharField(max_length=50)
    image_admin = models.ImageField(upload_to='image', default='k.jpeg')
    location_admin = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username


class Salle(models.Model):
    id_salle = models.AutoField(primary_key=True)
    nom_salle = models.CharField(max_length=50)
    capacite = models.IntegerField()
    est_disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_salle


class Section(models.Model):
    id_section = models.IntegerField(primary_key=True, default=10)
    nom_section = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_section



class Groupe(models.Model):
    id_groupe = models.IntegerField(primary_key=True)
    nom_groupe = models.CharField(max_length=50)

    def __str__(self):
        return self.nom_groupe

# Liste des noms de groupe
noms_groupes = [
    "Groupe 1",
    "Groupe 2"
]



class Etudiant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    id_user = models.IntegerField(null=True, blank=True)
    nom_etudiant = models.CharField(max_length=45)
    prenom_etudiant = models.CharField(max_length=50)
    image_etudiant = models.ImageField(upload_to='image', default='k.jpeg')
    location_etudiant = models.CharField(max_length=100, blank=True)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE, blank=True, default=1)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, default=1)


    def __str__(self):
        return self.nom_etudiant
    
    def get_nom(self):
        return self.nom_etudiant
    
    def get_prenom(self):
        return self.prenom_etudiant
    
    def get_location(self):
        return self.location_etudiant

    def get_image(self):
        return self.image_etudiant

    def get_groupe(self):
        return self.groupe.nom_groupe
    
    def get_section(self):
        return self.section.nom_section




class Module(models.Model):
    id_module = models.IntegerField(primary_key=True)
    nom_module = models.CharField(max_length=100)
    abreviation_nom_module = models.CharField(max_length=10, blank=True, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return self.nom_module

    def get_presences(self):
        return Presence.objects.filter(exam__module=self)    

# Liste des noms de module
noms_modules = [
    "Securité Informatique",
    "Systeme d'Exploitation",
    "Bussness Inteligence",
    "Données Semi-Structure",
    "Redaction Scientifique",
    "Recherche d'Information",
    "Genie Locigiel",
    "Administration de Système d'Information",
    "Systeme d'Aide à la Décision",
    "Developement Web"
]
# Liste des abréviations correspondantes
abreviations_modules = [
    "SI",
    "SE2",
    "BI",
    "DSS",
    "RS",
    "RI",
    "GL",
    "ASI",
    "SAD",
    "DW"
]
# Vérification du nombre de noms de module et d'abréviations
assert len(noms_modules) == len(abreviations_modules), "Le nombre de noms de module et d'abréviations doit être identique."
# Création des instances de Module
for i in range(len(noms_modules)):
    Module.objects.get_or_create(
        id_module=i+1,
        defaults={
            'nom_module': noms_modules[i],
            'abreviation_nom_module': abreviations_modules[i]
        }
    )



class Enseignant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    id_user = models.IntegerField()
    nom_enseignant = models.CharField(max_length=50)
    prenom_enseignant = models.CharField(max_length=50)
    image_enseignant = models.ImageField(upload_to='image', default='k.jpeg')
    grade_enseignant = models.CharField(max_length=100)
    location_enseignant = models.CharField(max_length=100, blank=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username    

    def get_nom(self):
        return self.nom_enseignant
    
    def get_prenom(self):
        return self.prenom_enseignant
    
    def get_location(self):
        return self.location_enseignant
    


def get_nom_module(self, obj):
    return obj.enseignant.module.nom_module


class Surveillant(models.Model):
    enseignant = models.ForeignKey(Administrateur, on_delete=models.CASCADE)
    id_surveillant = models.IntegerField()

    def __str__(self):
        return str(self.enseignant)




# Création des instances de Groupe
# for nom_groupe in noms_groupes:
#     section_par_defaut = Section.objects.first()  # Récupère la première section existante (vous pouvez ajuster cela selon vos besoins)
#     Groupe.objects.get_or_create(nom_groupe=nom_groupe, section=section_par_defaut)



class Examen(models.Model):
    id_exam = models.IntegerField(primary_key=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.enseignant.module.nom_module
    


class Presence(models.Model):
    #etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    etudiant = models.ManyToManyField(Etudiant)
    #salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    #section = models.ForeignKey(Section, on_delete=models.CASCADE, default='1')
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, default=1)
    id_presence = models.IntegerField(primary_key=True)
    marque_presence = models.BooleanField(default=False)
    #groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id_presence)



# class User(models.Model):
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=15)
#     dob = models.DateField(null=True)
    

#     def __str__(self):
#         return str(self.name)
     

