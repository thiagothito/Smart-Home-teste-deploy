from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import get_object_or_404

from .models import Usuario

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['nome', 'email', 'senha', 'nascimento', 'endereco', 'cep']
    template_name = 'usuarios/login.html'
    success_url = reverse_lazy('home')

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = ['nome', 'email', 'senha', 'nascimento', 'endereco', 'cep']
    template_name = 'usuarios/cadastro.html'
    success_url = reverse_lazy('home')

class UsuarioDelete(DeleteView):
    model = Usuario
    template_name = 'cadastros/formulario-excluir.html'
    success_url = reverse_lazy('home')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um com esse username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'login.html')

        return HttpResponse('usuário cadastrado com sucesso')
    

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password = senha)

        if user:
            login_django(request, user)
                        
            context = {'name' : user}
            return render(request, 'paginas/perfil.html', context)

            

            #return HttpResponse(user)
            
                    
                       
        else: 
                    
            return HttpResponse('usuário ou senha inválidos')
        
        


class HomePageView(TemplateView):
    template_name = 'paginas/home.html'


class QuemSomosView(TemplateView):
    template_name = 'paginas/quem_somos.html'
    
class PerfilView(TemplateView):
    template_name = 'paginas/perfil.html'


