from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm, CriarUsuarioForm

# ----------------------------
# LOGIN / LOGOUT
# ----------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario:
            login(request, usuario)

            # Redireciona de acordo com o tipo
            if usuario.tipo == 'coordenador':
                return redirect('home_coordenador')
            elif usuario.tipo == 'professor':
                return redirect('home_professor')
            elif usuario.tipo == 'estudante':
                return redirect('home_estudante')
            else:
                messages.error(request, "Tipo de usuário inválido.")
                logout(request)
                return redirect('login')
        else:
            messages.error(request, "Usuário ou senha incorretos.")

    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ----------------------------
# PERFIL
# ----------------------------
@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            # Redireciona conforme tipo de usuário
            if request.user.tipo == 'coordenador':
                return redirect('home_coordenador')
            elif request.user.tipo == 'professor':
                return redirect('home_professor')
            else:
                return redirect('home_estudante')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})


@login_required
def ver_perfil(request):
    return render(request, 'ver_perfil.html', {'usuario': request.user})


# ----------------------------
# CRIAR USUÁRIO (somente coordenador)
# ----------------------------
@login_required
def criar_usuario(request):
    if request.user.tipo != 'coordenador':
        messages.error(request, "Acesso negado!")
        return redirect('login')

    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Salva senha corretamente
            usuario.set_password(form.cleaned_data['senha'])
            # Salva matrícula
            usuario.matricula = form.cleaned_data.get('matricula', '')
            usuario.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('home_coordenador')
    else:
        form = CriarUsuarioForm()

    return render(request, 'criar_usuario.html', {'form': form})
