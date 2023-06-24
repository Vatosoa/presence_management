import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from datetime import date

from .models import Administrateur, Enseignant, Etudiant, Presence, Salle, Module, Section, Groupe
# from .models import User
# from .forms import UserRegForm


#-- -----------------------------------------------------
#-- -----------------------------------------------------
#-- -----------------    HOME   -------------------------
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def home(request):
    return render(request, 'page_accueil.html')



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#-- SIGNUP - On a desactivé cette partie pour le sécurité du site --------------
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def signupAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "L'email est déjà utilisé")
                return redirect('inscription_admin')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Le nom d'utilisateur est déjà utilisé")
                return redirect('inscription_admin')
            else:  
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Connexion d'utilisateur vers le dashbord                                
                # créer un profile pour le nouveau utilisateur 
                user_model = User.objects.get(username=username)
                new_admin = Administrateur.objects.create(user=user_model, id_user=user_model.id)
                #new_admin.user.username = new_admin.nom_admin
                new_admin.save()
                return redirect('connexion_admin')
        else:
            messages.info(request, "Vous avez saisi deux différents mots de passe")
            return redirect('inscription_admin')
    else:
        return render(request, 'registration/inscription_admin.html')


def signupTeacher(request):    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "L'email est déjà utilisé")
                return redirect('inscription_enseignant')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Le nom d'utilisateur est déjà utilisé")
                return redirect('inscription_enseignant')
            else:  
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Connexion d'utilisateur vers le dashbord                                
                # créer un profile pour le nouveau utilisateur 
                user_model = User.objects.get(username=username)
                new_teacher = Enseignant.objects.create(user=user_model, id_user=user_model.id)
                new_teacher.save()
                return redirect('connexion_enseignant')
        else:
            messages.info(request, "Vous avez saisi deux différents mots de passe")
            return redirect('inscription_enseignant')
    else:
        return render(request, 'registration/inscription_enseignant.html')


def signupStudent(request):    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "L'email est déjà utilisé")
                return redirect('inscription_etudiant')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Le nom d'utilisateur est déjà utilisé")
                return redirect('inscription_etudiant')
            else:  
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Connexion d'utilisateur vers le dashbord                                
                # créer un profile pour le nouveau utilisateur 
                user_model = User.objects.get(username=username)
                new_student = Etudiant.objects.create(user=user_model, id_user=user_model.id)
                new_student.save()
                return redirect('connexion_etudiant')
        else:
            messages.info(request, "Vous avez saisi deux différents mots de passe")
            return redirect('inscription_etudiant')
    else:
        return render(request, 'registration/inscription_etudiant.html')



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#-- REGISTRATION -- SIGNIN -- LOGOUT ----------
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def signinAdmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try: 
            user_auth = auth.authenticate(username=username, password=password)
            user_model = User.objects.get(username=username)
            user_exist = User.objects.filter(username=username, password=password).exists()
            etudiant_exist = Etudiant.objects.filter(user=user_model, id_user=user_model.id).exists()
            enseignant_exist = Enseignant.objects.filter(user=user_model, id_user=user_model.id).exists()            
            if((user_auth is not None) and (user_exist == etudiant_exist) and (user_exist == enseignant_exist)):
                auth.login(request, user_auth)
                return redirect('tableau_de_bord_admin')            
            else:
                messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
                return redirect('connexion_admin')
        except:
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
            return redirect('connexion_admin')
    else:
        return render(request,'registration/connexion_admin.html')


def signinTeacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try: 
            user_auth = auth.authenticate(username=username, password=password)
            user_model = User.objects.get(username=username)
            user_exist = User.objects.filter(username=username, password=password).exists()
            etudiant_exist = Etudiant.objects.filter(user=user_model, id_user=user_model.id).exists()
            admin_exist = Administrateur.objects.filter(user=user_model, id_user=user_model.id).exists()                        
            if((user_auth is not None) and (user_exist == etudiant_exist) and (user_exist == admin_exist)):
                auth.login(request, user_auth)
                return redirect('tableau_de_bord_enseignant')
            else:
                messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
                return redirect('connexion_enseignant')
        except:
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
            return redirect('connexion_enseignant')
    else:
        return render(request, 'registration/connexion_enseg.html')


def signinStudent(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try: 
            user_auth = auth.authenticate(username=username, password=password)
            user_model = User.objects.get(username=username)
            user_exist = User.objects.filter(username=username, password=password).exists()
            enseignant_exist = Enseignant.objects.filter(user=user_model, id_user=user_model.id).exists()
            admin_exist = Administrateur.objects.filter(user=user_model, id_user=user_model.id).exists()            
            if((user_auth is not None) and (user_exist == enseignant_exist) and (user_exist == admin_exist)):    
                auth.login(request, user_auth)
                return redirect('tableau_de_bord_etudiant')
            else:
                messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
                return redirect('tableau_de_bord_etudiant')
        except: 
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
            return redirect('connexion_etudiant')
    else:
        return render(request, 'registration/connexion_etudiant.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  DASHBOARD -- (ADMIN - TEACHER - STUDENT)  ---
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def dashboardAdmin(request):
     # Récupérer le module sélectionné
    module = Module.objects.get(id_module=1)  # Remplacez 1 par la logique pour obtenir le module sélectionné

    context = {
        'module': module,
    }

    return render(request, 'administrateur/Dashboard_Admin.html', context)

def dashboardTeacher(request):
    return render(request, 'enseignant/Dashboard_enseign.html')

def dashboardStudent(request):
    return render(request, 'etudiant/Dashboard_etudiant.html')



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  PROFIL -- (ADMIN - TEACHER - STUDENT) : USER ---
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def profileAdmin(request):
    try: 
        admin = Administrateur.objects.get(user=request.user)
        return render(request, 'administrateur/Profil_Admin.html', {'admin':admin})
    except:
        messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
        return redirect('connexion_admin')


@login_required(login_url='connexion_enseignant')
def profileTeacher(request):
    try: 
        teacher = Enseignant.objects.get(user=request.user)
        return render(request, 'enseignant/Profil_enseig.html', {'teacher':teacher})
    except:
        messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
        return redirect('connexion_enseignant')
    

def profileStudent(request):
    try: 
        student = Etudiant.objects.get(user=request.user)
        return render(request, 'etudiant/Profil_etudiant.html', {'student':student})
    except:
        messages.info(request, "Le nom d'utilisateur ou le mot de passe est invalide")
        return redirect('connexion_etudiant')


def profileUser(request):
    students = Etudiant.objects.all()
    teachers = Enseignant.objects.all()
    context = {
        'students':students,
        'teachers':teachers,
    }
    return render(request, 'utilisateur/Gestionutil_admin.html', context)


def listRoom(request):
    salles = Salle.objects.all()
    return render(request, 'salle/liste_salle.html', {'salles':salles})


def listPresenceTeacher(request):
    presence = Presence.objects.all()
    module = Module.objects.all()
    etudiant = Etudiant.objects.all()
    enseignant = Enseignant.objects.all()
    context = {
        'presence':presence,
        'module':module,
        'etudiant': etudiant,
        'enseignant': enseignant,
    }
    return render(request, 'enseignant/verification_enseign.html',context)


def listPresence(request):
    module = Module.objects.all()
    presences = Presence.objects.all()
    context = {
        'presences':presences,
        'module':module,
    }
    return render(request, 'etudiant/verification_etudiant.html', context)




# def voir_presence_module(request, enseignant_id, module_id):
#     enseignant = Enseignant.objects.get(id_enseignant=enseignant_id)
#     module = Module.objects.get(id_module=module_id)
#     presences = module.get_presences()
#     context = {
#         'enseignant': enseignant,
#         'module': module,
#         'presences': presences
#     }
#     return render(request, 'enseignant/presence_module.html', context)

def moduleStudentT(request, id_module):
    module = Module.objects.get(pk=id_module)
    presence = Presence.objects.filter(module=module)
    context = {
        'module': module,
        'presence': presence
    }
    return render(request, 'enseignant/module_etudiant.html', context)


#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  CREER -- USER, ROOM,  ---
#-- -----------------------------------------------------
#-- -----------------------------------------------------
@login_required
def createUser(request):
    # groupe = Groupe.objects.all()
    # module = Module.objects.all()
    if request.method == 'POST':
        # Récupérer les informations du nouvel utilisateur depuis la requête POST
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']  # Rôle de l'utilisateur (administrateur, enseignant, étudiant)        
        # Créer un nouvel utilisateur avec le nom d'utilisateur et le mot de passe fournis
        user = User.objects.create_user(username=username, password=password)
        # Assigner le rôle approprié à l'utilisateur en fonction de la valeur du champ "role"
        if role == 'administrateur':
            user.is_superuser = True
            user.is_staff = True
            administrateur = Administrateur(user=user, id_user=1)
            administrateur.save()
        elif role == 'enseignant':
            user.is_staff = True
            enseignant = Enseignant(user=user, id_user=1)
            enseignant.save()
        elif role == 'etudiant':
            user.is_staff = False
            etudiant = Etudiant(user=user, id_user=1)
            etudiant.save()
        # Enregistrer les modifications de l'utilisateur
        
        #  # Récupérer les valeurs des champs spécifiques au rôle sélectionné
        # if role == 'etudiant':
        #     groupe_nom = request.POST['nom_groupe']
        #     # Vérifier si le groupe existe déjà
        #     groupe, created = Groupe.objects.get_or_create(nom_groupe=groupe_nom)
        #     # Ajouter l'étudiant au groupe s'il n'est pas déjà présent
        #     if etudiant not in groupe.etudiant.all():
        #         groupe.etudiant.add(etudiant)            
        #mety ny an'ilay enseignant
        # elif role == 'enseignant':
        #     grade_enseignant = request.POST['grade_enseignant']
        #     module_id = request.POST['nom_module']
        #     module = Module.objects.get(id_module=module_id)
        #     enseignant, created= Enseignant.objects.get_or_create(user=user, id_user=1, defaults={'grade_enseignant': grade_enseignant, 'module': module})
        #     if not created:
        #         enseignant.grade_enseignant = grade_enseignant
        #     enseignant.save()

        #     #Associer l'enseignant au module
        #     module.enseignant = enseignant
        #     module.save()


        user.save()
        # Rediriger vers une page de confirmation ou effectuer d'autres actions
        return redirect('gestion_utilisateur_admin') 
    # context = {
    #     'groupe': groupe,
    #     'module': module,
    # }   
    return render(request, 'utilisateur/ajouter_utilisateur.html')


@login_required
def createRoom(request):
    if request.method == 'POST':
        # Récupérer les informations de la nouvelle salle depuis la requête POST
        nom_salle = request.POST['nom_salle']
        capacite = request.POST['capacite']
        est_disponible = request.POST.get('est_disponible', False) == 'on'
        # Créer un nouvel objet Salle avec les attributs fournis
        salle = Salle.objects.create(nom_salle=nom_salle, capacite=capacite, est_disponible=est_disponible)
        # Enregistrer la nouvelle salle dans la base de données
        salle.save()
        # Rediriger vers une page de confirmation ou effectuer d'autres actions
        return redirect('liste_salle')
    
    return render(request, 'salle/ajouter_salle.html')


#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  MODIFIER (ADMIN - TEACHER - STUDENT : USER) ---
#-- -----------------------------------------------------
#-- -----------------------------------------------------
def updateAdminProfile(request, id):
    admin = Administrateur.objects.get(user=request.user.id)
    if request.method == 'POST':
        #Recupere les données du formulaire modifier
        nouveau_nom_user = request.POST['username']
        nouveau_nom_admin= request.POST['nom_admin']
        nouveau_prenom_admin = request.POST['prenom_admin']
        nouveau_password = request.POST['password']
        nouveau_email = request.POST['email']
        nouveau_image_admin = request.POST['image_admin']
        nouveau_location_admin = request.POST['location_admin']
        #mettre à jour les info de l'admin
        admin.user.username = nouveau_nom_user
        admin.nom_admin = nouveau_nom_admin
        admin.prenom_admin = nouveau_prenom_admin
        admin.user.password = nouveau_password
        admin.user.email = nouveau_email
        admin.image_admin = nouveau_image_admin
        admin.location_admin = nouveau_location_admin
        #enregistrer        
        admin.user.save()
        admin.save()
        # admin.nom_admin == admin.user.username
        return redirect('profile_admin')     
    return render(request, 'administrateur/Modifier_Profil_Admin.html', {'admin':admin})


def updateTeacherProfile(request, id):
    teacher = Enseignant.objects.get(user=request.user.id)
    if request.method == 'POST':
        #Recupere les données du formulaire modifier
        nouveau_nom_user = request.POST['username']
        nouveau_nom_enseignant= request.POST['nom_enseignant']
        nouveau_prenom_enseignant = request.POST['prenom_enseignant']
        nouveau_password = request.POST['password']
        nouveau_email = request.POST['email']
        nouveau_image_enseignant = request.POST['image_enseignant']
        nouveau_location_enseignant = request.POST['location_enseignant']
        #mettre à jour les info de l'admin
        teacher.user.username = nouveau_nom_user
        teacher.nom_enseignant = nouveau_nom_enseignant
        teacher.prenom_enseignant = nouveau_prenom_enseignant
        teacher.user.password = nouveau_password
        teacher.user.email = nouveau_email
        teacher.image_enseignant = nouveau_image_enseignant
        teacher.location_enseignant = nouveau_location_enseignant
        #enregistrer        
        teacher.user.save()
        teacher.save()
        # admin.nom_admin == admin.user.username
        return redirect('profile_enseignant') 
    return render(request, 'enseignant/Modifier_Profil_Teacher.html', {'teacher': teacher})


def updateStudentProfile(request, id):
    student = Etudiant.objects.get(user=request.user.id)
    if request.method == 'POST':
        #Recupere les données du formulaire modifier
        nouveau_nom_user = request.POST['username']
        nouveau_nom_etudiant= request.POST['nom_etudiant']
        nouveau_prenom_etudiant = request.POST['prenom_etudiant']
        nouveau_password = request.POST['password']
        nouveau_email = request.POST['email']
        nouveau_image_etudiant = request.FILES['image_etudiant']
        nouveau_location_etudiant = request.POST['location_etudiant']
        #mettre à jour les info de l'admin
        
        student.user.username = nouveau_nom_user
        student.nom_etudiant = nouveau_nom_etudiant
        student.prenom_etudiant = nouveau_prenom_etudiant
        student.user.password = nouveau_password
        student.user.email = nouveau_email
        student.location_etudiant = nouveau_location_etudiant
        if 'image_etudiant' in request.FILES:
            nouveau_image_etudiant = request.FILES['image_etudiant']
            # Enregistrer l'image dans le dossier "media"
            student.image_etudiant = nouveau_image_etudiant
        #enregistrer        
        student.user.save()
        student.save()
        # admin.nom_admin == admin.user.username
        return redirect('profile_etudiant')
    return render(request, 'etudiant/Modifier_Profil_etudiant.html', {'student':student})



@login_required
def updateTeacherUser(request, id):
    utilisateur = get_object_or_404(Enseignant, id=id)
    modules = Module.objects.all()
    if request.method == 'POST':
        nom = request.POST['nom_enseignant']
        prenom = request.POST['prenom_enseignant']
        location = request.POST['location_enseignant']
        nom_module = request.POST['nom_module']

        #Mettre à jour enseignant #donnée à modifier ne peut pas s'afficher
        utilisateur.nom_enseignant = nom
        utilisateur.prenom_enseignant = prenom
        utilisateur.location_enseignant = location

        # Mettre à jour la clé étrangère module de l'utilisateur
        module = Module.objects.get(id_module=nom_module)
        utilisateur.module = module

        if 'image_enseignant' in request.FILES:
            image_enseignant = request.FILES['image_enseignant']
            # Enregistrer l'image dans le dossier "media"
            utilisateur.image_enseignant = image_enseignant
            utilisateur.save()
        return redirect('gestion_utilisateur_admin')
    context = {
        'utilisateur':utilisateur,
        'modules':modules,
    }
    return render(request, 'utilisateur/Modifierutilen_admin.html', context)



def updateStudentUser(request, id):
    utilisateur = get_object_or_404(Etudiant, id=id)
    groupes = Groupe.objects.all()
    sections = Section.objects.all()
    if request.method == 'POST':
        # Traitement de la soumission du formulaire
        nom = request.POST['nom_etudiant']
        prenom = request.POST['prenom_etudiant']
        location = request.POST['location_etudiant']
        image_etudiant = request.FILES['image_etudiant']
        nom_groupe = request.POST['nom_groupe']
        nom_section = request.POST['nom_section']
        # Mettre à jour les attributs de l'utilisateur
        utilisateur.nom_etudiant = nom
        utilisateur.prenom_etudiant = prenom
        utilisateur.location_etudiant = location
        #utilisateur.image_etudiant = image_etudiant
        utilisateur.groupe.nom_groupe = nom_groupe
        utilisateur.section.nom_section = nom_section
        if 'image_etudiant' in request.FILES:
            image_etudiant = request.FILES['image_etudiant']
#             # Enregistrer l'image dans le dossier "media"
            utilisateur.image_etudiant = image_etudiant
        # Enregistrer les modifications dans la base de données
        utilisateur.save()
        # Rediriger vers une autre page ou afficher un message de succès
        return redirect('gestion_utilisateur_admin')
    context = {
        'utilisateur': utilisateur,
        'groupes': groupes,
        'sections': sections,
    }
    return render(request, 'utilisateur/Modifierutilet_admin.html', context)


@login_required
def updateRoom(request, id):    
    salle = Salle.objects.get(id_salle=id)
    if request.method == 'POST':
        nouveau_nom = request.POST['nom_salle']
        nouveau_capacite = request.POST['capacite']
        nouveau_disponible = request.POST.get('est_disponible') == 'on'
        #Mettre à jour etudiant #donnée à modifier ne peut pas s'afficher
        salle.nom_salle = nouveau_nom
        salle.capacite = nouveau_capacite
        salle.est_disponible = nouveau_disponible
        salle.save()
        return redirect('liste_salle')
    
    return render(request, 'salle/modifier_liste_salle.html', {'salle':salle})



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  SUPPRIMER -- ( ADMIN - TEACHER - STUDENT ): USER --
#-- -----------------------------------------------------
#-- -----------------------------------------------------
@login_required
def deleteAdminProfile(request,id):
    admin = Administrateur.objects.get(user=request.user.id)
    if request.method == 'POST':
        #supprim
        admin.user.delete()
        admin.delete()
        return redirect('/')
    return render(request, 'administrateur/Supprimer_Profil_Admin.html', {'admin':admin})


def deleteTeacherProfile(request, id):
    teacher = Enseignant.objects.get(user=request.user.id)
    if request.method == 'POST':
        #supprim
        teacher.user.delete()
        teacher.delete()
        return redirect('/')
    return render(request, 'enseignant/Supprimer_Profil_Teacher.html', {'teacher':teacher})


def deleteStudentProfile(request, id):
    student = Etudiant.objects.get(user=request.user.id)
    if request.method == 'POST':
        #supprim
        student.user.delete()
        student.delete()
        return redirect('/')
    return render(request, 'etudiant/Supprimer_Profil_etudiant.html', {'student':student})


@login_required
def deleteTeacherUser(request, id):
    utilisateur = get_object_or_404(Enseignant, id=id)
    if request.method == 'POST':
        #supprim
        utilisateur.user.delete()
        utilisateur.delete()
        return redirect('gestion_utilisateur_admin')
    context = {
        'utilisateur':utilisateur
    }
    return render(request, 'utilisateur/Supprimer_en_util.html', context)


@login_required
def deleteStudentUser(request, id):
    utilisateur = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
        utilisateur.user.delete()
        utilisateur.delete()
        return redirect('gestion_utilisateur_admin')
    context = {
        'utilisateur': utilisateur,
    }
    return render(request, 'utilisateur/Supprimer_et_util.html', context)



def deleteRoom(request, id):
    salle = get_object_or_404(Salle, id_salle=id)

    if request.method == 'POST':
        salle.delete()
        return redirect('liste_salle')

    return render(request, 'salle/supprimer_salle.html', {'salle': salle})    



#-- -----------------------------------------------------
#-- -----------------------------------------------------
#--  ADMIN APPROUVER (TEACHER - STUDENT : USER), On n'a plus besoin parce que le SIGNUP est desactivé ---
#-- -----------------------------------------------------
#-- -----------------------------------------------------
@login_required
def approveTeacherUser(request, id): 
    pass


@login_required
def approveStudentUser(request,id):
    pass
     

# à revoir
# import pandas as pd

# def import_students(request):
#     if request.method == 'POST' and request.FILES['file']:
#         file = request.FILES['file']
        
#         if file.name.endswith('.xlsx'):
#             # Lecture du fichier Excel
#             df = pd.read_excel(file)
#         elif file.name.endswith('.csv'):
#             # Lecture du fichier CSV
#             df = pd.read_csv(file)
#         else:
#             # Gérer les autres formats de fichiers si nécessaire
#             return HttpResponse('Format de fichier non pris en charge.')

#         # Parcourir les lignes du DataFrame
#         for index, row in df.iterrows():
#             id_user = row['id_user']
#             nom_etudiant = row['Nom']
#             prenom_etudiant = row['Prénom']
#             location_etudiant = row['location_etudiant']
#             image_etudiant = row['image_etudiant']
#             groupe = row['groupe']
#             groupe = Groupe.objects.get(nom_groupe=groupe)
#             section = row['section']
#             section, created = Section.objects.get_or_create(nom_section=section)

#             # Récupérer d'autres colonnes si nécessaire

#             # Créer un nouvel objet Etudiant et enregistrer dans la base de données
#             etudiant = Etudiant(
#                 nom_etudiant=nom_etudiant,
#                 prenom_etudiant=prenom_etudiant,
#                 id_user = id_user,
#                 location_etudiant = location_etudiant,
#                 image_etudiant = image_etudiant,
#                 groupe = groupe,
#                 section = section,
#                 # Affecter d'autres valeurs aux champs appropriés
#             )
#             etudiant.save()

#         return HttpResponse('Importation réussie.')
    
#     return render(request, 'utilisateur/Gestionutil_admin.html')




# def add(request):
#     if request.method == 'POST':
#         form = UserRegForm(request.POST)
#         if form.is_valid():
#             form.save()
#         form = UserRegForm()
#     else:
#         form = UserRegForm()
#     return render(request, 'useregistration/add.html', {'form': form})


# def show(request):
#     users = User.objects.all()
#     return render(request, 'useregistration/show.html', {'users': users})


# def authenticate(request, id):
#     user = User.objects.get(pk=id)
#     user.is_authenticated = True
#     user.save()
#     return redirect('show')

# def approved_list(request):
#     users = User.objects.all()
#     a_users = [u for u in users if u.is_authenticated==True]
#     for au in a_users:
#         print(au.name)
#     return render(request, 'useregistration/approvedusers.html', {'ausers':a_users})    

# def update(request, id):
#     if request.method == 'POST':
#         user = User.objects.get(pk=id)
#         form = UserRegForm(request.POST, instance=user)
#         if form.is_valid():
#             form.save()
#             return redirect('show')
#     else:
#         user = User.objects.get(pk=id)
#         form = UserRegForm(instance=user)
#     return render(request, 'useregistration/userupdate.html', {'form':form})

# def delete(request, id):
#     user = User.objects.get(pk=id)
#     user.delete()
#     return redirect('show')