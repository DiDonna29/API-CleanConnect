# users/models.py
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings

# --- MANAGER (SERVICIO DE CREACIÓN DE USUARIOS) ---
class CustomUserManager(BaseUserManager):
    """
    Manager que define la lógica de creación de usuarios para CustomUser.
    """
    def create_user(self, email, full_name=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        # Asegura que el superusuario tenga los permisos correctos por defecto
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        # Asigna el rol de negocio de superadmin
        extra_fields.setdefault('role', 'superadmin') 
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, full_name, password, **extra_fields)


# --- USERS (CORE) ---
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Sobreescribimos el campo username para usar el email como campo de login
    username = None 
    email = models.EmailField(unique=True) 
    
    auth0_id = models.CharField(max_length=200, unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    
    ROLE_CHOICES = [
        ("cleaner", "Cleaner"),
        ("host", "Host"),
        ("admin", "Admin"),
        ("superadmin", "Superadmin"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="host")
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = CustomUserManager()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} ({self.role})"


# --- PERFILES ---
class CleanerProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cleaner_profile')
    
    bio = models.TextField(blank=True)
    services = models.JSONField(default=list, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    location = models.CharField(max_length=200, blank=True)
    rating_avg = models.FloatField(default=0)
    total_reviews = models.IntegerField(default=0)
    availability = models.JSONField(default=dict, blank=True)
    stripe_account_id = models.CharField(max_length=200, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class HostProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='host_profile')
    address_default = models.CharField(max_length=300, blank=True, null=True)
    payment_method_info = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)