from django.urls import path

from .views import HomePageView, PerfilView, QuemSomosView, UsuarioCreate, UsuarioUpdate

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('cadastrar/usuario/', UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path('quem_somos/', QuemSomosView.as_view(), name="quem_somos"),
    path('atualizar-dados/<int:pk>', 
         UsuarioUpdate.as_view(), name='atualizar-dados'),
    
    path('perfil/<int:pk>', PerfilView.as_view(), name="perfil"),

   

]