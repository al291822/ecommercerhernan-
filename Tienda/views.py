from django.shortcuts import render

def store(request):
     context = {}
     return render(request, 'Tienda/Tienda.html', context)

def cart(request):
     context = {}
     return render(request, 'Tienda/carrito.html', context)

def checkout(request):
      context = {}
      return render(request, 'Tienda/comprar.html', context)
