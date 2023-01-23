from django.shortcuts import render, redirect
from .models import Lekarze, Specjalizacja, Recepta, Wizyta
from .forms import WizytaForm, LekarzeForm, SpecjalizacjaForm, ReceptaForm, SkierowanieForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Zostało stworzone konto: '+ user)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password )
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Nazwa użytkownika lub hasło są niepoprawne')

    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
def dodaj_lekarza(request):
    submitted = False
    if request.method == "POST":
        form =LekarzeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_lekarza?submitted=True')
    else:
        form = LekarzeForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'dodaj_lekarza.html',{'form':form, 'submitted': submitted})

@login_required(login_url='login')
def dodaj_wizyte(request):
    submitted = False
    if request.method == "POST":
        form = WizytaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_wizyte?submitted=True')
    else:
        form = WizytaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'dodaj_wizyte.html',{'form':form, 'submitted': submitted})
def dodaj_specjalizacje(request):
    submitted = False
    if request.method == "POST":
        form = SpecjalizacjaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_wizyte?submitted=True')
    else:
        form = SpecjalizacjaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'dodaj_specjalizacje.html',{'form':form, 'submitted': submitted})
def dodaj_recepte(request):
    submitted = False
    if request.method == "POST":
        form = ReceptaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_recepte?submitted=True')
    else:
        form = ReceptaForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'dodaj_recepte.html',{'form':form, 'submitted': submitted})


def index(request):
    specjalizacje = Specjalizacja.objects.all()
    dane = {'specjalizacje': specjalizacje}
    return render(request, 'szablon.html', dane)

def specjalizacja (request, id):
    specjalizacja_user = Specjalizacja.objects.get(pk=id)
    specjalizacja_lekarz = Lekarze.objects.filter(specjalizacja=specjalizacja_user)
    specjalizacje = Specjalizacja.objects.all()
    dane = {'specjalizacja_user': specjalizacja_user,
            'specjalizacja_lekarz': specjalizacja_lekarz,
            'specjalizacje': specjalizacje}
    return render(request, 'specjalizacja_lekarz.html', dane)

def lekarz (request, id):
    lekarz_user = Lekarze.objects.get(pk=id)
    specjalizacje = Specjalizacja.objects.all()
    dane = {'lekarz_user': lekarz_user, 'specjalizacje': specjalizacje}
    return render(request, 'lekarz.html', dane)

def kontakt (request):
    kontakt = Specjalizacja.objects.all()
    dane ={'kontakt': kontakt}
    return render(request, 'kontakt.html', dane)
@login_required(login_url='login')

def wizyta (request):
    wizyta_user = Wizyta.objects.all()
    wizyta=Specjalizacja.objects.all()
    dane ={'wizyta_user':wizyta_user, 'wizyta': wizyta}
    return render(request, 'wizyta.html', dane)

def dodaj_skierowanie(request):
    submitted = False
    if request.method == "POST":
        form = SkierowanieForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dodaj_skierowanie?submitted=True')
    else:
        form = SkierowanieForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'dodaj_skierowanie.html',{'form':form, 'submitted': submitted})

