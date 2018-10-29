from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Perfil
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView 
# Create your views here.

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm
    def form_valid(self, form):
        form_save()
        usuario = form.cleaned_data.get('username')
        rut = form.cleaned_data.get('rut')
        nombres = form.cleaned_data.get('nombres')
        apellidos = form.cleaned_data.get('apellidos')
        nacimiento = form.cleaned_data.get('nacimiento')
        telefono = form.cleaned_data.get('telefono')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data('password1')
        usuario = authenticate(username = usuario, password=password)
        login(self.request, usuario)
        return redirect('/')

class BienvenidaView(TemplateView):
    template_name = 'web/MisPerris.html'

class SignInView(LoginView):
    template_name = 'web/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

class InfoView(TemplateView):
    template_name = 'web/quienes_somos.html'

class ContactView(TemplateView):
    template_name = 'web/contactanos.html'

class ServicioView(TemplateView):
    template_name = 'web/servicios.html'