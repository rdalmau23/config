from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label="Correu electrònic")
    password = forms.CharField(widget=forms.PasswordInput, label="Contrasenya")
