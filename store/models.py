from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Table client
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name

"""Le modèle de produit sera composé d'un "nom", "prix" et numérique(digital). 
   Le numérique sera simplement vrai ou faux et nous indiquera s'il s'agit d'un 
   produit numérique ou d'un produit physique qui doit être expédié.
"""

# Table produit
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    """"@property : est un decorator Python qui transforme la méthode 
        en propriété accessible sans parenthèses, comme si 
        c'était un attribut du modèle
    """
    
    # facilite la gestion des images des produits, en gérant les cas
    # où une image n'est pas présente.
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
# Table commande
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
# Table article commander(Panier)
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

# Table Addresse de livraison
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address