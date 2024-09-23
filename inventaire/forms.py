from django import forms
from .models import Produit, Fournisseur, Commande, Client,ProduitCommande

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'

# class CommandeProduitForm(forms.ModelForm):    
#     class Meta:
#         model = CommandeProduit
#         fields = '__all__'


        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['prenom', 'nom', 'adresse', 'telephone']
        
        
# class CommandeProduitForm(forms.ModelForm):
#     class Meta:
#         model = CommandeProduit
#         fields = ['client', 'produit', 'quantite', 'prix_vente']

class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client']

class ProduitCommandeForm(forms.ModelForm):
    class Meta:
        model = ProduitCommande
        fields = ['produit', 'quantite', 'prix_vente']
        


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')