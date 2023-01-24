from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product

# Create your views here.
def get_home(request):
    return HttpResponse("<h1> Welcome to the website</h1>")

def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    return HttpResponse(f"<h1>{product.name}</h1> <p> {product.description}</p> Price: <p>{product.price}</p>")
