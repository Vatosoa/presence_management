from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/admin', views.signupAdmin, name='inscription_admin'),
    path('signup/teacher', views.signupTeacher, name='inscription_enseignant'),
    path('signup/student', views.signupStudent, name='inscription_etudiant'),
    path('signin/admin', views.signinAdmin, name='connexion_admin'),
    path('signin/teacher', views.signinTeacher, name='connexion_enseignant'),
    path('signin/student', views.signinStudent, name='connexion_etudiant'),
    path('profile/admin', views.profileAdmin, name='profile_admin'),
    path('profile/admin/dashboard', views.dashboardAdmin, name='tableau_de_bord_admin'),
    path('profile/admin/room', views.listRoom, name='liste_salle' ),
    path('profile/teacher', views.profileTeacher, name='profile_enseignant'),
    path('profile/teacher/dashboard', views.dashboardTeacher, name='tableau_de_bord_enseignant'),
    path('profile/teacher/presence', views.listPresenceTeacher, name='verification_presence_enseignant'),
    path('profile/student', views.profileStudent, name='profile_etudiant'),
    path('profile/student/dashboard', views.dashboardStudent, name='tableau_de_bord_etudiant'),
    path('profile/user', views.profileUser, name='gestion_utilisateur_admin'),
    path('profile/student/presence/', views.listPresence, name='liste_presence'),
    path('logout', views.logout, name='logout'),
    path('profil//update/admin=<int:id>', views.updateAdminProfile, name='modifier_profile_admin'),
    path('profil/update/teacher=<int:id>', views.updateTeacherProfile, name='modifier_profile_enseignant'),
    path('profil/update/student=<int:id>', views.updateStudentProfile, name='modifier_profile_etudiant'),
    path('user/update/teacher=<int:id>', views.updateTeacherUser, name='modifier_utilisateur_enseignant'),
    path('user/create', views.createUser, name='ajouter_utilisateur'),
    path('room/create', views.createRoom, name='ajouter_salle'),
    path('user/update/student=<int:id>', views.updateStudentUser, name='modifier_utilisateur_etudiant'),
    path('room/update/room=<int:id>', views.updateRoom, name='modifier_liste_salle'),
    path('profil/delete/admin=<int:id>', views.deleteAdminProfile, name='supprimer_profile_admin'),
    path('profil/delete/teacher=<int:id>', views.deleteTeacherProfile, name='supprimer_profile_enseignant'),
    path('profil/delete/student=<int:id>', views.deleteStudentProfile, name='supprimer_profile_etudiant'),
    path('user/delete/teacher=<int:id>', views.deleteTeacherUser, name='supprimer_utilisateur_enseignant'),
    path('user/delete/student=<int:id>', views.deleteStudentUser, name='supprimer_utilisateur_etudiant'),
    path('room/delete/room=<int:id>', views.deleteRoom, name='supprimer_salle'),
    path('user/approve/teacher=<int:id>', views.approveTeacherUser, name='approuver_utilisateur_enseignant'),
    path('user/approve/student=<int:id>', views.approveStudentUser, name='approuver_utilisateur_etudiant'),
    path('student/module/<int:id_module>/student/', views.moduleStudentT, name='module_etudiant'),
    #path('import-students/', views.import_students, name='import_students'),


    # path('add/', views.add, name='add'),
    # path('show/', views.show, name='show'),
    # path('approve/<int:id>', views.authenticate, name='approve'),
    # path('approvedlist/', views.approved_list, name='approvedlist'),
    # path('update/<int:id>', views.update, name='update'),
    # path('delete/<int:id>', views.delete, name='delete'),


]

