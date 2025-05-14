from django.contrib import admin
from cars.models import Car,Brand,Fuel_type


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Fuel_typeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model','brand',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Fuel_type, Fuel_typeAdmin)