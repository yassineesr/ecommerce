from django.urls import path
from .views import Home,checkout,panier,compte,search,detail,ajouter_au_panier, supprimer,passer_commande,passer_commande1,passer_commande2,lire_fichier_json
urlpatterns = [
    path('',Home,name='Home'),
    path('checkout',checkout,name='checkout'),
    path('panier',panier,name='panier'),
    path('compte',compte,name='compte'),   
    path('search', search, name='search'),
    path('detail/<int:id>', detail, name='detail'),
    path('ajouter_au_panier/<int:id>', ajouter_au_panier, name='ajouter_au_panier'),
    path('supprimer/<int:id>', supprimer, name='supprimer'),
    path('passer-commande/', passer_commande, name='passer_commande'),
    path('passer-commande1/', passer_commande1, name='passer_commande1'),
    path('passer-commande2/', passer_commande2, name='passer_commande2'),
    path('lire_fichier_json/', lire_fichier_json, name='lire_fichier_json'),

] 