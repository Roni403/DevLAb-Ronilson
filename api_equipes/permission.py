from rest_framework.permissions import BasePermission

class IsProfessorOrCoordenador(BasePermission):
    message = "Apenas professor ou coordenador podem realizar essa ação."

    def has_permission(self, request, view):
        usuario = request.user

        # caso o usuário não esteja autenticado
        if not usuario.is_authenticated:
            return False

        return usuario.cargo in ["professor", "coordenador"]
