from django.contrib import admin
from django.urls import path, include
from api_projetos.views import home, redirecionar_usuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Página inicial (só acessa logado)
    path('', home, name='home'),

    # Login e Logout
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),

    # Redirecionamento pós-login
    path('accounts/redirect/', redirecionar_usuario, name='redirect_user'),

    # APIs
    path('api/alunos/', include('api_usuarios.urls')),
    path('api/projetos/', include('api_projetos.urls')),
]
