from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate

from app.forms import LoginForm
from app.models import Usuari


def login(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            usuari = Usuari.objects.filter(email=email, password=password).first()
            if usuari:
                request.session['usuari_id'] = usuari.id
                return redirect('inici')
            else:
                error = "Credencials incorrectes"
    else:
        form = LoginForm()
    return render(request, './login.html', {"form": form, "error": error})

def logout_view(request):
    request.session.flush()
    return redirect('login')

