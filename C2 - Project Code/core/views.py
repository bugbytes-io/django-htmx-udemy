from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST' and 'HX-Request' in request.headers:
        product_name = request.POST.get('product')
        product = {'id': 107, 'name': product_name}
        return render(request, 'partials/product-row.html', {'product': product})
    context = {}
    return render(request, 'index.html', context)

def about(request):
    if 'HX-Request' in request.headers:
        context = {}
        return render(request, 'partials/about.html', context)
    return HttpResponse("Imagine this was a full page...")

def products(request):
    context = {}
    return render(request, 'partials/products.html', context)    