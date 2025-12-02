from django.contrib import admin
from django.urls import path, include
from api_projetos import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial (só acessa logado)
    path('', views.home, name='home'),

    # Login
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),

    # Logout
    path(
        'accounts/logout/',
        views.sair,  # usando a view de logout do views.py
        name='logout'
    ),

    # Redirecionamento pós-login
    path('accounts/redirect/', views.redirecionar_usuario, name='redirect_user'),

    # APIs
    path('api/alunos/', include('api_usuarios.urls')),
    path('api/projetos/', include('api_projetos.urls')),
]
