from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Offer
# Create your views here.


def index(request):
    products = Product.objects.all()
    offer = Offer.objects.all()
    return render(request, 'main/products.html',{"products":products,"offer":offer})
def products(response):
    return render(response,'main/base.html',{})

def product(request):
    return HttpResponse("product view")
