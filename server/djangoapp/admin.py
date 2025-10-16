'''Admin configuration for CarMake and CarModel models.'''

from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    '''Inline admin interface for CarModel within CarMake admin.'''
    model = CarModel


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    '''Admin interface for CarModel.'''
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
    '''Admin interface for CarMake with inline CarModel.'''
    fields = [
        'name',
        'description',
        'country',
        'is_active',
    ]
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)


admin.site.register(CarModel, CarModelAdmin)
