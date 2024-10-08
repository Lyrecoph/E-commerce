from django.contrib import admin

from store.models import *
 
# Register your models here.

# Personnaliser l'interface d'admin
admin.site.site_header = "Mon Administration"
admin.site.site_title = "Administration de E-comm"
admin.site.index_title = "Bienvenue sur l'interface d'administration"


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'user')  # Affiche ces colonnes dans la liste
    search_fields = ('name', 'email')  # Barre de recherche par nom ou email
    list_filter = ('user',)  # Filtres pour filtrer par utilisateur associé
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital')  # Affiche ces colonnes
    search_fields = ('name',)  # Barre de recherche par nom de produit
    list_filter = ('digital',)  # Filtres pour filtrer par produits numériques ou non
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')  # Colonnes affichées
    search_fields = ('transaction_id',)  # Recherche par ID de transaction
    list_filter = ('complete', 'date_ordered')  # Filtres par état de la commande et date

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'date_added')  # Colonnes affichées
    list_filter = ('product', 'date_added')  # Filtrer par produit et date
    
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'city', 'state', 'zipcode', 'order')  # Colonnes affichées
    search_fields = ('city', 'zipcode')  # Barre de recherche par ville ou code postal
    list_filter = ('city', 'state')  # Filtrer par ville et état
   
   
""""gérer plusieurs modèles directement à partir d'une même vue d'administration, 
    tu peux utiliser les "inline models" pour afficher et gérer les relations 
    directement dans le formulaire d'un modèle principal.
""" 
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # Nombre de lignes vides à afficher dans le formulaire

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')
    inlines = [OrderItemInline]  # Ajoute les OrderItems à la vue de commande


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)

