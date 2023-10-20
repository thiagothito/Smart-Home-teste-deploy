from django.urls import path
from . import views
from .views import HomePageView, QuemSomosView, UsuarioCreate, UsuarioDelete, UsuarioUpdate

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('quem-somos/', QuemSomosView.as_view(), name="quem-somos"),
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('excluir/usuario/<int:pk>',
         UsuarioDelete.as_view(), name="excluir-usuario"),
    path('login/', views.login, name='login'),
    path('atualizar-dados/', UsuarioUpdate.as_view(), name='atualizar-dados'),
    #path('plataforma/', views.plataforma, name='plataforma'),
]