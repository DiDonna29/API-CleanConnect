# users/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, CleanerProfile, HostProfile
from .serializers import UserSerializer, CleanerProfileSerializer, HostProfileSerializer

# ViewSet para exponer la información del usuario autenticado y CRUD de perfiles
class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # Solo el usuario autenticado puede ver/editar su propio perfil
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    
class CleanerProfileViewSet(viewsets.ModelViewSet):
    queryset = CleanerProfile.objects.all()
    serializer_class = CleanerProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CleanerProfile.objects.filter(user=self.request.user)

class HostProfileViewSet(viewsets.ModelViewSet):
    queryset = HostProfile.objects.all()
    serializer_class = HostProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HostProfile.objects.filter(user=self.request.user)