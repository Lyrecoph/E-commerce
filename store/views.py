from django.shortcuts import render

from store.models import *

# Create your views here.

def store(request):
    # récupèrer dans un queryset l'ensemble des produits
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)