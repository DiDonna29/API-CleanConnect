# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, CleanerProfile, HostProfile

# 1. Registrar CustomUser con personalizaciones
class CustomUserAdmin(UserAdmin):
    # Campos que se muestran en la lista de usuarios
    list_display = ('email', 'full_name', 'role', 'is_staff', 'is_active')
    # Campos por los que se puede filtrar
    list_filter = ('role', 'is_staff', 'is_active')
    # Campos que se pueden buscar
    search_fields = ('email', 'full_name')
    # Campos que se pueden editar en la creación de un nuevo usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('full_name', 'role')}),
    )
    # Reemplazamos la configuración de fieldsets para mostrar solo los campos necesarios en el cambio
    fieldsets = (
        (None, {'fields': ('email', 'password', 'auth0_id')}),
        ('Personal info', {'fields': ('full_name', 'phone', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('email',)

# Registrar el modelo de usuario principal
admin.site.register(CustomUser, CustomUserAdmin)
# Registrar los perfiles
admin.site.register(CleanerProfile)
admin.site.register(HostProfile)