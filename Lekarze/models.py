from datetime import datetime

from django.db import models
from django.contrib.auth import authenticate, login, logout, get_user
from django.http import request
from django.contrib.auth.models import User

class Specjalizacja(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.TextField(blank=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Specjalizacja"
        verbose_name_plural = "Specjalizacje"

# Create your models here.
class Lekarze(models.Model):

    specjalizacja = models.ForeignKey(Specjalizacja, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    sala = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.imie and self.nazwisko

    class Meta:
        verbose_name = "Lekarz"
        verbose_name_plural = "Lekarze"


class Wizyta (models.Model):
    lekarz = models.ForeignKey(Lekarze, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.IntegerField(max_length=11)
    data = models.DateField()

    def __str__(self):
        return (self.imie)

    class Meta:
        verbose_name = "Wizyta"
        verbose_name_plural = "Wizyty"

class Lek(models.Model):

    numer_leku = models.DecimalField(max_digits=5, decimal_places=0)
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Lek"
        verbose_name_plural = "Leki"

class Recepta(models.Model):
    lek = models.ForeignKey(Lek, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nazwisko

    class Meta:
        verbose_name = "Recepta"
        verbose_name_plural = "Recepty"

class Badanie(models.Model):

    numer_badania= models.DecimalField(max_digits=5, decimal_places=0)
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Badanie"
        verbose_name_plural = "Badania"

class Skierowanie(models.Model):
    badanie = models.ForeignKey(Badanie, on_delete=models.CASCADE, null=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    pesel = models.DecimalField(max_digits=11, decimal_places=0)

    def __str__(self):
        return self.nazwisko

    class Meta:
        verbose_name = "Skierowanie"
        verbose_name_plural = "Skierowania"