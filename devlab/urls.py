from django.contrib import admin
from django.urls import path, include
from api_projetos import views as projetos_views
from api_usuarios import views as usuarios_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home (decide a home pelo tipo do usuário)
    path('', projetos_views.home, name='home'),

    # Login e Logout
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='registration/login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),
    path(
        'accounts/logout/',
        projetos_views.sair,
        name='logout'
    ),

    # Botões da home
    path('usuarios/<str:tipo>/', usuarios_views.usuarios_filtrados, name='usuarios_filtrados'),
    path('projetos/lista/', projetos_views.lista_projetos, name='lista_projetos'),
    path('equipes/lista/', projetos_views.lista_equipes, name='lista_equipes'),

    # APIs
    path('api/alunos/', include('api_usuarios.urls')),
    path('api/projetos/', include('api_projetos.urls')),
]
