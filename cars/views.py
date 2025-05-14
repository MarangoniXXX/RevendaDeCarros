from django.shortcuts import render
from django.template import Template


def cars_views(request):
    return render(
        request, 
        'cars.html',
        {'cars':{'model':'Astra'} }
    )       