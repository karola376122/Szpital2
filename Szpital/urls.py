"""Szpital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Lekarze.views import specjalizacja
from Lekarze.views import lekarz
from Lekarze.views import kontakt
from Lekarze.views import wizyta
from Lekarze.views import dodaj_wizyte
from Lekarze.views import logoutUser
from Lekarze.views import loginPage, registerPage
from Lekarze.views import index
from Lekarze.views import dodaj_lekarza
from Lekarze.views import dodaj_specjalizacje
from Lekarze.views import dodaj_recepte
from Lekarze.views import dodaj_skierowanie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('specjalizacja/<id>/', specjalizacja, name='specjalizacja'),
    path('lekarz/<id>/', lekarz, name='lekarz'),
    path('kontakt', kontakt, name='kontakt'),
    path('dodaj_wizyte', dodaj_wizyte, name='dodaj_wizyte'),
    path('register/', registerPage, name="register"),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('dodaj_lekarza', dodaj_lekarza, name='dodaj_lekarza'),
    path('dodaj_specjalizacje', dodaj_specjalizacje, name='dodaj_specjalizacje'),
    path('dodaj_recepte', dodaj_recepte, name='dodaj_recepte'),
    path('dodaj_skierowanie', dodaj_skierowanie, name='dodaj_skierowanie'),

]