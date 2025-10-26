# jobs/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

class JobViewSet(viewsets.ModelViewSet):
    # Lógica de ViewSet para listar y modificar trabajos
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        # Admin ve todo. Host ve sus trabajos. Cleaner ve abiertos o asignados.
        if user.role in ['admin', 'superadmin']:
            return Job.objects.all().order_by('-created_at')
        if user.role == 'host':
            return Job.objects.filter(host=user).order_by('-created_at')
        if user.role == 'cleaner':
            return Job.objects.filter(
                Q(status='open') | Q(assigned_to=user)
            ).distinct().order_by('-created_at')
        return Job.objects.none()

class ApplicationViewSet(viewsets.ModelViewSet):
    # Lógica de ViewSet para listar y modificar postulaciones
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        
        # Cleaner ve sus aplicaciones. Host ve aplicaciones a sus trabajos.
        if user.role == 'cleaner':
            return Application.objects.filter(cleaner=user)
        if user.role == 'host':
            return Application.objects.filter(job__host=user)

        # Admin/Superadmin ven todo
        return Application.objects.all().order_by('-created_at')