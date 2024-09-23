from django.contrib import admin
from .models import Fournisseur, Produit, Commande, Client,ProduitCommande

admin.site.register(Fournisseur)
admin.site.register(Produit)
admin.site.register(ProduitCommande)
admin.site.register(Commande)
admin.site.register(Client)
