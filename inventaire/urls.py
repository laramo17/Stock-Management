from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    
    
    path('', views.dashboard, name='dashboard'),
    #path('dashboard/', views.dashboard, name='dashboard'),

    path('produit/', views.produit_page, name='produit'),
    path('fournisseurs/', views.fournisseur_page, name='fournisseur'),
    path('fournisseur/fournisseur_form', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('liste_fournisseur/fournisseurs/', views.fournisseurs_view, name='liste_fournisseur'),
    path('modifier_fournisseur/fournisseur_details/<int:fournisseur_id>/', views.fournisseur_details, name='fournisseur_details'),
    path('modifier_fournisseur/', views.modifier_fournisseur, name='modifier_fournisseur'),
    #Produit
    path('produit/produit_form', views.ajouter_produit, name='ajouter_produit'),
    #path('produit/supprimer_produit', views.supprimer_produit, name='supprimer_produit'),
    path('modifier_produit/produit_details/<int:produit_id>/', views.produit_details, name='produit_details'),
    path('liste_produit/', views.produits_view, name='liste_produit'),
    path('modifier_produit/', views.modifier_produit, name='modifier_produit'),
    #path('commande/commande_form', views.ajouter_commande, name='ajouter_commande'),
    #COMMANDE
    
    path('commande/commande_form', views.ajouter_commande, name='ajouter_commande'),
    path('commandes/', views.commande_page, name='commande'),
    path('liste_commande/', views.commandes_view, name='liste_commande'),
    path('modifier_commande/', views.modifier_commande, name='modifier_commande'),
    path('modifier_commande/commande_details/<int:commande_id>/', views.commande_details, name='commande_details'),
    #Client
    path('client/', views.client_page, name='client'),
    path('clients/', views.clients_view, name='liste_clients'),
    path('ajouter_client/', views.ajouter_client, name='ajouter_client'),
    path('modifier_client/client_details/<int:client_id>/', views.client_details, name='client_details'),
    path('modifier_client/', views.modifier_client, name='modifier_client'),
    
    
    
    
    
    
    
    
    
    
    
    path('logout/', views.logout_view, name='logout'),
]
