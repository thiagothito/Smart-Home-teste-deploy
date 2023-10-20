from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from .models import Usuario



class HomePageView(TemplateView):
    template_name = 'paginas/home.html'


class QuemSomosView(TemplateView):
    template_name = 'paginas/quem_somos.html'

class PerfilView(TemplateView):
    template_name = 'paginas/perfil.html'

class UsuarioUpdate(UpdateView):
    template_name = 'usuarios/cadastro.html'
    
class UsuarioCreate(TemplateView):
    template_name = 'usuarios/login.html'







