   
from django.db import models
class Fournisseur(models.Model):
    idF = models.AutoField(primary_key=True)
    nomF = models.CharField(max_length=255)
    adresseF = models.TextField()

    def __str__(self):
        return self.nomF

class Produit(models.Model):
    idP = models.AutoField(primary_key=True)
    nomP = models.CharField(max_length=255)
    quantite_stock = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.nomP

class Client(models.Model):
    idCl = models.AutoField(primary_key=True)
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# class CommandeProduit(models.Model):
#     id = models.AutoField(primary_key=True)
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
#     quantite = models.IntegerField()
#     prix_vente = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Commande de {self.client} - {self.produit.nomP} (x{self.quantite})"


class Commande(models.Model):
    idC = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.client} du {self.date}"

class ProduitCommande(models.Model):
    idPC = models.AutoField(primary_key=True)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_vente = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Produit {self.produit.nomP} (x{self.quantite}) de la commande {self.commande}"
    
    


