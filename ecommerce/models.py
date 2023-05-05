from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    def __str__(self):
        return self.nom
   
class Product(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
   
