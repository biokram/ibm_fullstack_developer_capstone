'''Define the data models for CarMake and CarModel.
'''

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    '''Model representing a car manufacturer.'''
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        '''Return the name as the string representation.'''
        return self.name


class CarModel(models.Model):
    '''Model representing a specific car model.'''
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2000),
        ])

    def __str__(self):
        '''Return the name as the string representation.'''
        return self.name  # Return the name as the string representation
