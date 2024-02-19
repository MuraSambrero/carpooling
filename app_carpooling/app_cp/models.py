from django.db import models
from django.contrib.auth.models import AbstractUser

class CityA(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Cities for point A"

    def __str__(self):
        return self.name

class CityB(models.Model):
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = "Cities for point B"

    def __str__(self):
        return self.name
    
class Car(models.Model):
    name = models.CharField(max_length=20, unique=True)
    place_in = models.IntegerField()

    class Meta:
        verbose_name_plural = "Cars"

    def __str__(self):
        return self.name

class User(AbstractUser):
    tel = models.CharField("Телефон", max_length=15, blank=True, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'tel', 'car_name']

    def __str__(self):
        return self.username

class Trip(models.Model):
    citya = models.ForeignKey(CityA, on_delete=models.CASCADE)
    cityb = models.ForeignKey(CityB, on_delete=models.CASCADE)
    departure_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    arrive_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    place_in_car = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Trip from {self.citya.name} to {self.cityb.name} city'

