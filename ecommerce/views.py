from django.shortcuts import render,get_object_or_404,redirect,HttpResponse,HttpResponseRedirect
from .models import Product,Client,Commande
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from bs4 import BeautifulSoup
import requests
import csv
import json

def Home(request):
    produits = Product.objects.all()
    paginator = Paginator(produits,3)
    page = request.GET.get('page' ,1)
    try:
        produits_page = paginator.page(page)
    except PageNotAnInteger:
        # Si le numéro de page n'est pas un entier, renvoyer la première page.
        produits_page = paginator.page(1)
    except EmptyPage:
        # Si le numéro de page est plus grand que le nombre total de pages, renvoyer la dernière page.
        produits_page = paginator.page(paginator.num_pages)
    
    return render(request, 'produits.html', {'produits':   produits_page })

def checkout(request):
    return render(request,'checkout.html')  
def compte(request):
    return render(request,'compte.html')
def search(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__contains=query)
    return render(request, 'produits.html', {'produits': products})

def detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'detail.html', {'product': product})



def panier(request):
    panier = []
    if 'panier' in request.session:
        panier_ids = request.session['panier']
        panier = Product.objects.filter(id__in=panier_ids)
        
    return render(request, 'panier.html', {'panier': panier})

def ajouter_au_panier(request, id):
    produit = get_object_or_404(Product, id=id)
    if 'panier' not in request.session:
        request.session['panier'] = {}
    if id not in request.session['panier']:
        request.session['panier'][id] = {'id': id, 'nom': produit.name, 'prix': float(produit.price), 'quantite': 1}
    else:
        request.session['panier'][id]['quantite'] += 1
    request.session.modified = True
    return redirect('Home')

def supprimer(request, id):
    produit = get_object_or_404(Product, id=id)
    if 'panier' in request.session:
        panier = request.session['panier']
        if str(id) in panier:
            del panier[str(id)]
            request.session.modified = True
    return redirect('panier')


def checkout(request):
    panier = []
    if 'panier' in request.session:
        panier_ids = request.session['panier']
        panier = Product.objects.filter(id__in=panier_ids)
        
    context = {'panier': panier}
    return render(request, 'checkout.html', context=context)   

def passer_commande(request):
    total=0
    if request.method == 'POST':
         total = float(request.POST.get('Total'))
    return render(request, 'auth.html',{'total':total}) 

    
    
      
def passer_commande1(request):
    
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        adresse = request.POST['adresse']
        email = request.POST['email']
        telephone = request.POST['telephone']
        pw = request.POST['pw']
        client = Client(nom=nom, prenom=prenom, adresse=adresse, email=email,password=pw, telephone=telephone)
        client.save()
        client_id = client.id
        
        total = float(request.POST.get('Total'))
        date = timezone.now()
        
        commande = Commande(client_id=client_id, date=date, total=total)
        commande.save()
        request.session.flush()
        return render(request, 'felicitation.html') 
        
    else:
        return HttpResponse('non merci')         

def passer_commande2(request):
    if request.method == 'POST':
        user = request.POST['user']
        pw = request.POST['pw']
        client = Client.objects.filter(email=user, password=pw).first()
        if(client!=None):
              client_id = client.id
              total = float(request.POST.get('Total'))
              date = timezone.now()
              commande = Commande(client_id=client_id, date=date, total=total)
              commande.save()
              request.session.flush()
              return render(request, 'felicitation.html') 
        else:
            return HttpResponse('email ou mot de passe incorrecte')      
    else:
        return HttpResponse('non merci') 

def read_json_file(fichier):
    with open(fichier) as f:
        data = json.load(f)
    return data

def lire_fichier_json(fichier):
    data = read_json_file(fichier)
    for item in data:
        img=item['link']
        desc=item['title']
        nom="lap"
        prix=float(100)
        pr=Product(name=nom, description=desc, price=prix, image=img)
        pr.save()

lire_fichier_json('./data.json')


    
    
    
