# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    """
    Model representing a car manufacturer/make (e.g., Toyota, Ford, BMW)
    """
    
    # Basic Information
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Name of the car manufacturer"
    )
    
    description = models.TextField(
        blank=True,
        help_text="Description of the car make"
    )
    
    # Additional Fields
    country = models.CharField(
        max_length=100,
        blank=True,
        help_text="Country of origin"
    )
    
    is_active = models.BooleanField(
        default=True,
        help_text="Whether the make is currently active"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Car Make'
        verbose_name_plural = 'Car Makes'
    
    def __str__(self):
        """
        String representation of the CarMake object
        """
        return self.name
    
    def get_model_count(self):
        """
        Returns the number of car models associated with this make
        (Assumes a related CarModel model exists with a ForeignKey to CarMake)
        """
        return self.carmodel_set.count() if hasattr(self, 'carmodel_set') else 0


class CarModel(models.Model):
    """
    Model representing a specific car model (e.g., Toyota Camry, Ford Mustang)
    """
    
    # Car Type Choices
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    HATCHBACK = 'Hatchback'
    TRUCK = 'Truck'
    VAN = 'Van'
    
    CAR_TYPES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (HATCHBACK, 'Hatchback'),
        (TRUCK, 'Truck'),
        (VAN, 'Van'),
    ]
    
    # Many-to-One relationship with CarMake
    car_make = models.ForeignKey(
        'CarMake',  # Reference to CarMake model
        on_delete=models.CASCADE,
        related_name='car_models',
        help_text="The manufacturer of this car model"
    )
    
    # Dealer reference (from Cloudant database)
    dealer_id = models.IntegerField(
        help_text="ID of the dealer in Cloudant database"
    )
    
    # Basic Information
    name = models.CharField(
        max_length=100,
        help_text="Name of the car model (e.g., Camry, Mustang)"
    )
    
    car_type = models.CharField(
        max_length=20,
        choices=CAR_TYPES,
        default=SEDAN,
        help_text="Type of vehicle"
    )
    
    year = models.IntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2100)
        ],
        help_text="Model year"
    )
    
    # Additional Fields
    color = models.CharField(
        max_length=50,
        blank=True,
        help_text="Available color or primary color"
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Base price in USD"
    )
    
    mileage = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Current mileage (for used cars)"
    )
    
    fuel_type = models.CharField(
        max_length=20,
        choices=[
            ('Gasoline', 'Gasoline'),
            ('Diesel', 'Diesel'),
            ('Electric', 'Electric'),
            ('Hybrid', 'Hybrid'),
            ('Plug-in Hybrid', 'Plug-in Hybrid'),
        ],
        blank=True,
        help_text="Type of fuel"
    )
    
    transmission = models.CharField(
        max_length=20,
        choices=[
            ('Automatic', 'Automatic'),
            ('Manual', 'Manual'),
            ('CVT', 'CVT'),
        ],
        blank=True,
        help_text="Transmission type"
    )
    
    engine_size = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True,
        help_text="Engine size in liters"
    )
    
    horsepower = models.IntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0)],
        help_text="Engine horsepower"
    )
    
    description = models.TextField(
        blank=True,
        help_text="Detailed description of the car model"
    )
    
    is_available = models.BooleanField(
        default=True,
        help_text="Whether the model is currently available"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', 'car_make__name', 'name']
        verbose_name = 'Car Model'
        verbose_name_plural = 'Car Models'
        indexes = [
            models.Index(fields=['dealer_id']),
            models.Index(fields=['year']),
            models.Index(fields=['car_type']),
        ]
    
    def __str__(self):
        """
        String representation showing both car make and model
        """
        return f"{self.car_make.name} {self.name} ({self.year})"
    
    def get_full_name(self):
        """
        Returns the full name with type
        """
        return f"{self.year} {self.car_make.name} {self.name} {self.car_type}"
    
    def get_price_display(self):
        """
        Returns formatted price
        """
        if self.price:
            return f"${self.price:,.2f}"
        return "Price not available"
