from django.shortcuts import render, get_object_or_404, redirect
from .models import Produit, Fournisseur, Client, ProduitCommande, Commande

from .forms import ProduitForm, FournisseurForm, CommandeForm, ClientForm,ProduitCommandeForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after user creation
    else:
        form = UserCreationForm()
    return render(request, 'inventaire/add_user.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            # Authentication failed, display an error message
            error_message = "Invalid username or password"
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

# Dashboard view
# def dashboard(request):
#     # Récupérer le nombre total de chaque modèle
#     produits_count = Produit.objects.count()
#     fournisseurs_count = Fournisseur.objects.count()
#     commandes_count = Commande.objects.count()
#     clients_count = Client.objects.count()

#     context = {
#         'produits_count': produits_count,
#         'fournisseurs_count': fournisseurs_count,
#         'commandes_count': commandes_count,
#         'clients_count': clients_count,
#     }

#     return render(request, 'inventaire/dashboard.html', context)
def dashboard_view(request):
    return render(request, 'inventaire/dashboard.html')

def dashboard(request):
    produits_count = Produit.objects.count()
    fournisseurs_count = Fournisseur.objects.count()
    commandes_count = Commande.objects.count()
    clients_count = Client.objects.count()
    return render(request, 'inventaire/dashboard.html', {
        'produits_count': produits_count,
        'fournisseurs_count': fournisseurs_count,
        'commandes_count': commandes_count,
        'clients_count': clients_count,
    })

# def dashboard_view(request):
#     return render(request, 'inventaire/dashboard.html')

# def dashboard(request):
#     produits_count = Produit.objects.count()
#     fournisseurs_count = Fournisseur.objects.count()
#     commandes_count = Commande.objects.count()
#     return render(request, 'dashboard.html', {
#         'produits_count': produits_count,
#         'fournisseurs_count': fournisseurs_count,
#         'commandes_count': commandes_count,
#     })

def produit_page(request):
    return render(request, 'inventaire/produit.html')

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            produit = form.save()  # Sauvegarde les données du formulaire dans la base de données
            return redirect('produit')
        else:
            print(form.errors)  # Affiche les erreurs du formulaire dans le terminal pour le debug
    else:
        form = ProduitForm()

    fournisseurs = Fournisseur.objects.all()  # Récupère tous les fournisseurs de la base de données
    return render(request, 'inventaire/produit_form.html', {'form': form, 'fournisseurs': fournisseurs})


def produit_details(request, produit_id):
    produit = get_object_or_404(Produit, idP=produit_id)
    data = {
        'nomP': produit.nomP,
        'quantite_stock': produit.quantite_stock,
        'prix_unitaire': produit.prix_unitaire,
        'fournisseur': produit.fournisseur.idF,
    }
    return JsonResponse(data)


def modifier_produit(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        produit_id = request.POST.get('produit')
        produit = get_object_or_404(Produit, idP=produit_id)

        if action == "supprimer":
            produit.delete()
            return redirect('produit')  # Redirige vers la page qui liste les produits ou une page de succès

        elif action == "modifier":
            produit.nomP = request.POST.get('nomP')
            produit.quantite_stock = request.POST.get('quantite_stock')
            produit.prix_unitaire = request.POST.get('prix_unitaire')
            produit.fournisseur = get_object_or_404(Fournisseur, idF=request.POST.get('fournisseur'))
            produit.save()
            return redirect('produit')  # Redirige vers la page qui liste les produits ou une page de succès

    produits = Produit.objects.all()
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'inventaire/produit_modify.html', {'produits': produits, 'fournisseurs': fournisseurs})



def produits_view(request):
    produits = Produit.objects.all()
    context = {
        'produits': produits
    }
    return render(request, 'inventaire/table.html', context)


# Fournisseur views
def fournisseur_page(request):
    return render(request, 'inventaire/fournisseur.html')
# def fournisseur_form(request):
#     return render(request, 'inventaire/fournisseur_form.html')


def fournisseurs_view(request):
    fournisseurs = Fournisseur.objects.all()
    context = {
        'fournisseurs': fournisseurs
    }
    return render(request, 'inventaire/fournisseur_list.html', context)


def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            print("saved")
            return redirect('fournisseur') #redirection apres l'ajout
    else:
        form = FournisseurForm()
    return render(request, 'inventaire/fournisseur_form.html', {'form': form})

def fournisseur_details(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, idF=fournisseur_id)
    data = {
        'nomF': fournisseur.nomF,
        'adresseF': fournisseur.adresseF,
    }
    return JsonResponse(data)

def modifier_fournisseur(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        fournisseur_id = request.POST.get('fournisseur')
        fournisseur = get_object_or_404(Fournisseur, idF=fournisseur_id)

        if action == "supprimer":
            fournisseur.delete()
            return redirect('fournisseur')  # Redirige vers la page qui liste les fournisseurs ou une page de succès

        elif action == "modifier":
            fournisseur.nomF = request.POST.get('nomF')
            fournisseur.adresseF = request.POST.get('adresseF')
            fournisseur.save()
            return redirect('fournisseur')  # Redirige vers la page qui liste les fournisseurs ou une page de succès

    fournisseurs = Fournisseur.objects.all()
    return render(request, 'inventaire/fournisseur_modify.html', {'fournisseurs': fournisseurs})
#Client 
def client_page(request):
    return render(request, 'inventaire/client.html')

def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('client')
        else:
            print(form.errors)  # Affiche les erreurs du formulaire
    else:
        form = ClientForm()

    return render(request, 'inventaire/client-form.html', {'form': form})


def clients_view(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'inventaire/client_list.html', context)


def client_details(request, client_id):
    client = get_object_or_404(Client, idCl=client_id)
    data = {
        'prenom': client.prenom,
        'nom': client.nom,
        'telephone': client.telephone,
        'adresse': client.adresse,
    }
    return JsonResponse(data)

def modifier_client(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        client_id = request.POST.get('client')
        client = get_object_or_404(Client, idCl=client_id)

        if action == "supprimer":
            client.delete()
            return redirect('client')  # Redirige vers la page qui liste les clients ou une page de succès

        elif action == "modifier":
            client.prenom = request.POST.get('prenom')
            client.nom = request.POST.get('nom')
            client.telephone = request.POST.get('telephone')
            client.adresse = request.POST.get('adresse')
            client.save()
            return redirect('client')  # Redirige vers la page qui liste les clients ou une page de succès

    clients = Client.objects.all()
    return render(request, 'inventaire/client-modify.html', {'clients': clients})



def commande_page(request):
    return render(request, 'inventaire/commande.html')

def commandes_view(request):
    commandes = Commande.objects.all()
    context = {
        'commandes': commandes
    }
    return render(request, 'inventaire/commande_list.html', context)


def ajouter_commande(request):
    produits = Produit.objects.all()  # Récupérer tous les produits
    clients = Client.objects.all()  # Récupérer tous les clients
    
    if request.method == 'POST':
        client_id = request.POST.get('client')
        if client_id:
            client = Client.objects.get(pk=client_id)
            commande = Commande.objects.create(client=client)  # Créer une nouvelle commande
            
            produit_index = 0
            success = False
            error_message = None
            
            while f'produit_{produit_index}' in request.POST:
                produit_id = request.POST.get(f'produit_{produit_index}')
                quantite = request.POST.get(f'quantite_{produit_index}')
                prix_vente = request.POST.get(f'prix_vente_{produit_index}')
                
                if produit_id and quantite and prix_vente:
                    produit = Produit.objects.get(pk=produit_id)
                    quantite = int(quantite)
                    
                    if produit.quantite_stock >= quantite:
                        ProduitCommande.objects.create(
                            commande=commande,
                            produit=produit,
                            quantite=quantite,
                            prix_vente=prix_vente
                        )
                        
                        # Reduce the stock quantity of the product
                        produit.quantite_stock -= quantite
                        produit.save()
                        
                        success = True
                    else:
                        error_message = f"Not enough stock for {produit.nomP}"
                        break
                
                produit_index += 1
            
            if success:
                return redirect('commande')  # Rediriger vers une page de succès après l'ajout de la commande
            else:
                return render(request, 'inventaire/commande_form.html', {
                    'produits': produits, 
                    'clients': clients,
                    'error_message': error_message
                })
    
    # Si c'est une requête GET (première visite du formulaire), afficher le formulaire vide
    return render(request, 'inventaire/commande_form.html', {'produits': produits, 'clients': clients})


# def ajouter_commande(request):
#     produits = Produit.objects.all()  # Récupérer tous les produits
#     clients = Client.objects.all()  # Récupérer tous les clients
    
#     if request.method == 'POST':
#         client_id = request.POST.get('client')
#         if client_id:
#             client = Client.objects.get(pk=client_id)
#             commande = Commande.objects.create(client=client)  # Créer une nouvelle commande
            
#             produit_index = 0
#             success = False
            
#             while f'produit_{produit_index}' in request.POST:
#                 produit_id = request.POST.get(f'produit_{produit_index}')
#                 quantite = request.POST.get(f'quantite_{produit_index}')
#                 prix_vente = request.POST.get(f'prix_vente_{produit_index}')
                
#                 if produit_id and quantite and prix_vente:
#                     produit = Produit.objects.get(pk=produit_id)
                    
#                     ProduitCommande.objects.create(
#                         commande=commande,
#                         produit=produit,
#                         quantite=quantite,
#                         prix_vente=prix_vente
#                     )
                    
#                     success = True
                
#                 produit_index += 1
            
#             if success:
#                 return redirect('commande')  # Rediriger vers une page de succès après l'ajout de la commande
        
#         # Si quelque chose ne va pas, revenir au formulaire avec les données actuelles
#         return render(request, 'inventaire/commande_form.html', {'produits': produits, 'clients': clients})
    
#     # Si c'est une requête GET (première visite du formulaire), afficher le formulaire vide
#     return render(request, 'inventaire/commande_form.html', {'produits': produits, 'clients': clients})

# def ajouter_commande(request):
#     produits = Produit.objects.all()  # Récupérer tous les produits
#     clients = Client.objects.all()  # Récupérer tous les clients
    
#     if request.method == 'POST':
#         print("Form submitted")
#         commande_form = CommandeProduitForm(request.POST)
        
#         if commande_form.is_valid():
#             print("Commande form is valid")
#             commande = commande_form.save(commit=False)
#             client_id = request.POST.get('client')
#             if client_id:
#                 print(f"Client ID received: {client_id}")
#                 client = Client.objects.get(pk=client_id)
#                 commande.client = client
#                 commande.save()
                
#                 success = False
#                 produit_index = 0
                
#                 while f'produit_{produit_index}' in request.POST:
#                     produit_id = request.POST.get(f'produit_{produit_index}')
#                     quantite = request.POST.get(f'quantite_{produit_index}')
#                     prix_vente = request.POST.get(f'prix_vente_{produit_index}')
                    
#                     if produit_id and quantite and prix_vente:
#                         print(f"Produit ID: {produit_id}, Quantite: {quantite}, Prix vente: {prix_vente}")
#                         produit = Produit.objects.get(pk=produit_id)
                        
#                         CommandeProduit.objects.create(
#                             commande=commande,
#                             produit=produit,
#                             quantite=quantite,
#                             prix_vente=prix_vente
#                         )
                        
#                         success = True
                    
#                     produit_index += 1
                
#                 if success:
#                     print("Commande successfully saved")
#                     return redirect('commande')  # Rediriger vers une page de succès après l'ajout de la commande
                
#                 else:
#                     print("No produits were added to the commande")
#                     return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
            
#             else:
#                 print("Client ID not received")
#                 return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
        
#         else:
#             print("Commande form is not valid")
#             print("Errors:", commande_form.errors)
#             return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
    
#     else:
#         print("Form not submitted")
#         commande_form = CommandeProduitForm()
    
#     return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})


# def ajouter_commande(request):
#     produits = Produit.objects.all()  # Récupérer tous les produits
#     clients = Client.objects.all()  # Récupérer tous les clients
    
#     if request.method == 'POST':
#         commande_form = CommandeProduitForm(request.POST)
        
#         if commande_form.is_valid():
#             commande = commande_form.save(commit=False)
#             client_id = request.POST.get('client')
#             if client_id:
#                 client = Client.objects.get(pk=client_id)
#                 commande.client = client
#                 commande.save()
                
#                 success = False
#                 produit_index = 0
                
#                 while f'produit_{produit_index}' in request.POST:
#                     produit_id = request.POST.get(f'produit_{produit_index}')
#                     quantite = request.POST.get(f'quantite_{produit_index}')
#                     prix_vente = request.POST.get(f'prix_vente_{produit_index}')
                    
#                     if produit_id and quantite and prix_vente:
#                         produit = Produit.objects.get(pk=produit_id)
                        
#                         CommandeProduit.objects.create(
#                             commande=commande,
#                             produit=produit,
#                             quantite=quantite,
#                             prix_vente=prix_vente
#                         )
                        
#                         success = True
                    
#                     produit_index += 1
                
#                 if success:
#                     return redirect('commande')  # Rediriger vers une page de succès après l'ajout de la commande
                
#                 else:
#                     return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
            
#             else:
#                 return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
        
#         else:
#             return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})
    
#     else:
#         commande_form = CommandeProduitForm()
    
#     return render(request, 'inventaire/commande_form.html', {'commande_form': commande_form, 'produits': produits, 'clients': clients})





def modifier_commande(request,commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    produits_commande = ProduitCommande.objects.filter(commande=commande)
    
    context = {
        'commande': commande,
        'produits_commande': produits_commande,
    }
    return render(request, 'inventaire/commande-modify.html', {'commandes': context})

def commande_details(request, commande_id):
    commande = get_object_or_404(Commande, id=commande_id)
    produits_commandes = ProduitCommande.objects.filter(commande=commande)
    data = {
        'commande_id': commande.idC,
        'client_id': commande.client.idCl,
        'client_prenom': commande.client.prenom,
        'client_nom': commande.client.nom,
        'produits_commandes': list(produits_commandes.values('id', 'produit__idP', 'produit__nomP', 'quantite', 'prix_vente')),
    }
    return JsonResponse(data)

def commande_form(request):
    commandes = Commande.objects.all()
    return render(request, 'inventaire/commande-form.html', {'commandes': commandes})

def commande_details(request, commande_id):
    commande = get_object_or_404(Commande, idC=commande_id)
    client = commande.client
    produits_commandes = ProduitCommande.objects.filter(commande=commande)
    data = {
        'client_id': client.idCl,
        'produits': [
            {
                'produit_id': pc.produit.idP,
                'quantite': pc.quantite,
                'prix_vente': pc.prix_vente,
            } for pc in produits_commandes
        ]
    }
    return JsonResponse(data)

def modifier_commande(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        commande_id = request.POST.get('commande')
        commande = get_object_or_404(Commande, idC=commande_id)

        if action == "supprimer":
            # Restore stock quantities for products in the order
            produits_commande = ProduitCommande.objects.filter(commande=commande)
            for produit_commande in produits_commande:
                produit = produit_commande.produit
                produit.quantite_stock += produit_commande.quantite
                produit.save()
            
            commande.delete()
            return redirect('commande')  # Redirect to the page that lists the orders or a success page

        elif action == "modifier":
            client_id = request.POST.get('client')
            client = get_object_or_404(Client, idCl=client_id)
            commande.client = client
            commande.save()

            # Restore stock quantities for existing products
            produits_commande = ProduitCommande.objects.filter(commande=commande)
            for produit_commande in produits_commande:
                produit = produit_commande.produit
                produit.quantite_stock += produit_commande.quantite
                produit.save()

            # Delete existing product orders
            ProduitCommande.objects.filter(commande=commande).delete()

            # Add new products
            produits_ids = request.POST.getlist('produit')
            quantites = request.POST.getlist('quantite')
            prix_ventes = request.POST.getlist('prix_vente')

            for produit_id, quantite, prix_vente in zip(produits_ids, quantites, prix_ventes):
                produit = get_object_or_404(Produit, idP=produit_id)
                quantite = int(quantite)

                if produit.quantite_stock >= quantite:
                    ProduitCommande.objects.create(
                        commande=commande,
                        produit=produit,
                        quantite=quantite,
                        prix_vente=prix_vente
                    )
                    
                    # Reduce the stock quantity of the product
                    produit.quantite_stock -= quantite
                    produit.save()
                else:
                    error_message = f"Not enough stock for {produit.nomP}"
                    clients = Client.objects.all()
                    produits = Produit.objects.all()
                    commandes = Commande.objects.all()
                    return render(request, 'inventaire/commande-modify.html', {
                        'clients': clients,
                        'produits': produits,
                        'commandes': commandes,
                        'error_message': error_message
                    })

            return redirect('commande')  # Redirect to the page that lists the orders or a success page

    clients = Client.objects.all()
    produits = Produit.objects.all()
    commandes = Commande.objects.all()
    return render(request, 'inventaire/commande-modify.html', {
        'clients': clients,
        'produits': produits,
        'commandes': commandes
    })

# def modifier_commande(request):
#     if request.method == 'POST':
#         action = request.POST.get('action')
#         commande_id = request.POST.get('commande')
#         commande = get_object_or_404(Commande, idC=commande_id)

#         if action == "supprimer":
#             commande.delete()
#             return redirect('commande')  # Redirige vers la page qui liste les commandes ou une page de succès

#         elif action == "modifier":
#             client_id = request.POST.get('client')
#             client = get_object_or_404(Client, idCl=client_id)
#             commande.client = client
#             commande.save()

#             # Suppression des produits existants
#             ProduitCommande.objects.filter(commande=commande).delete()

#             # Ajout des nouveaux produits
#             produits_ids = request.POST.getlist('produit')
#             quantites = request.POST.getlist('quantite')
#             prix_ventes = request.POST.getlist('prix_vente')

#             for produit_id, quantite, prix_vente in zip(produits_ids, quantites, prix_ventes):
#                 produit = get_object_or_404(Produit, idP=produit_id)
#                 ProduitCommande.objects.create(
#                     commande=commande,
#                     produit=produit,
#                     quantite=quantite,
#                     prix_vente=prix_vente
#                 )

#             return redirect('commande')  # Redirige vers la page qui liste les commandes ou une page de succès

#     clients = Client.objects.all()
#     produits = Produit.objects.all()
#     commandes = Commande.objects.all()
#     return render(request, 'inventaire/commande-modify.html', {
#         'clients': clients,
#         'produits': produits,
#         'commandes': commandes
#     })
    
    
    
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')
