from django.shortcuts import render # type: ignore

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")

def welcome(request):
    return render(request,"welcome.html")

def lista(request):
    return render(request,"lista.html")

def chiSiamo(request):
    return render(request,"chiSiamo.html")

def variabili(request):
    context={
        'var1': 'Prima variabile',
        'var2': 'Seconda variabile',
        'var3': 'Terza variabile'
    }
    return render(request,"variabili.html",context)

def index(request):
    return render(request,"index.html")


