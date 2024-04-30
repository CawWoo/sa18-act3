from django.shortcuts import render

# Create your views here.
from .models import Product
from django.shortcuts import get_object_or_404


def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/index.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'myapp/show.html', {'product': product})



