from django.shortcuts import render
from django.template import Template
from .models import Car,Brand
from django.shortcuts import render, get_object_or_404


def home (request):
    carros = Car.objects.all()
    marcas = Brand.objects.all()

    #filtros
    brand = request.GET.get('brand')
    ano  = request.GET.get('ano')
    preco = request.GET.get('preco')


    if brand:
        carros = carros.filter(brand_id=brand)
    if ano:
         carros = carros.filter(factory_year=ano)
    if preco:
        carros = carros.filter(value_lte=preco)
    
    context = {
        'carros': carros,
        'marcas': marcas
    }
    return render(request, 'home.html', context)

def car_detail(request, car_id):
    carro = get_object_or_404(Car, pk=car_id)

    context = {
        'carro': carro
    }
    return render(request, 'car_detail.html', {'carro': carro})