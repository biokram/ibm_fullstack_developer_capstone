from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = [
        'CarMake', 
        'name', 
        'car_type', 
        'year', 
        'color', 
        'mileage', 
        'transmission', 
        'description', 
        'price', 
        'is_available', 
    ]


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = [
        'name', 
        'description', 
        'country', 
        'is_active', 
    ]
    
    inlines = [CarModelInline] 


admin.site.register(CarMake, CarMakeAdmin)


admin.site.register(CarModel, CarModelAdmin)
