from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm, CriarUsuarioForm
from django.db.models import Q
from .models import Usuario


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(request, username=username, password=password)

        if usuario:
            login(request, usuario)

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


@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('home_estudante')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'editar_perfil.html', {'form': form})


@login_required
def ver_perfil(request):
    return render(request, 'ver_perfil.html', {'usuario': request.user})


@login_required
def criar_usuario(request):
    if request.user.tipo != 'coordenador':
        messages.error(request, "Acesso negado!")
        return redirect('login')

    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['senha'])
            usuario.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect('listar_usuarios')
    else:
        form = CriarUsuarioForm()

    return render(request, 'criar_usuario.html', {'form': form})


@login_required
def listar_usuarios(request):
    if request.user.tipo != 'coordenador':
        messages.error(request, "Acesso negado!")
        return redirect('login')

    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(
            Q(username__icontains=query) | Q(matricula__icontains=query)
        )
    else:
        usuarios = Usuario.objects.all()

    return render(request, 'listar_usuarios.html', {
        'usuarios': usuarios,
        'query': query
    })


@login_required
def editar_usuario(request, usuario_id):
    if request.user.tipo != 'coordenador':
        messages.error(request, "Acesso negado!")
        return redirect('login')

    usuario = get_object_or_404(Usuario, id=usuario_id)

    if request.method == 'POST':
        form = CriarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Se a senha foi preenchida, atualiza
            senha = form.cleaned_data.get('senha')
            if senha:
                usuario.set_password(senha)
            usuario.save()
            messages.success(request, "Usuário atualizado com sucesso!")
            return redirect('listar_usuarios')
    else:
        # Preenche o form com os dados existentes
        form = CriarUsuarioForm(instance=usuario)

    return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})
