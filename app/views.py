from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Usuari
from .forms import LoginForm

def login(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuari = Usuari.objects.filter(email=email, password=password).first()
            if usuari:
                return render(request, './home.html', {"usuari": usuari})
            else:
                error = "Credencials incorrectes"
    else:
        form = LoginForm()
    return render(request, './login.html', {"form": form, "error": error})
