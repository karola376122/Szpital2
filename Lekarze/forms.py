from django import forms
from django.forms import ModelForm
from django.forms.widgets import NumberInput
from .models import Wizyta, Lekarze, Specjalizacja, Recepta, Skierowanie
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class DateForm(forms.Form):
    date = forms.DateField(input_formats=['%d/%m/%Y'])

class WizytaForm(ModelForm):
    class Meta:
        model = Wizyta
        fields = ('lekarz', 'imie', 'nazwisko', 'pesel', 'data')

        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control'}),
            'pesel': forms.TextInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date'}),

        }
class LekarzeForm(ModelForm):
    class Meta:
        model = Lekarze
        fields = ('specjalizacja', 'imie', 'nazwisko', 'sala')

        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control'}),
            'sala': forms.TextInput(attrs={'class':'form-control'}),
        }

class SpecjalizacjaForm(ModelForm):
    class Meta:
        model = Specjalizacja
        fields = ('nazwa', 'opis')

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control'}),
            'opis': forms.TextInput(attrs={'class':'form-control'}),
        }
class ReceptaForm(ModelForm):
    class Meta:
        model = Recepta
        fields = ('lek', 'imie','nazwisko', 'pesel')

        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class': 'form-control'}),
            'pesel': forms.TextInput(attrs={'class': 'form-control'})
        }

class SkierowanieForm(ModelForm):
    class Meta:
        model = Skierowanie
        fields = ('badanie', 'imie','nazwisko', 'pesel')

        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class': 'form-control'}),
            'pesel': forms.TextInput(attrs={'class': 'form-control'})
        }
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']
