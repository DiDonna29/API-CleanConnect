# users/serializers.py
from rest_framework import serializers
from .models import CustomUser, CleanerProfile, HostProfile

# Serializer Base de Usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'auth0_id', 'email', 'full_name', 'phone', 'role', 'is_active', 'created_at')
        read_only_fields = ('id', 'auth0_id', 'role', 'created_at')

# Serializer de Perfil de Cleaner
class CleanerProfileSerializer(serializers.ModelSerializer):
    # Relaciona el perfil con la info básica del usuario
    user = UserSerializer(read_only=True) 
    
    class Meta:
        model = CleanerProfile
        fields = '__all__'
        read_only_fields = ('id', 'user', 'rating_avg', 'total_reviews')

# Serializer de Perfil de Host
class HostProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = HostProfile
        fields = '__all__'
        read_only_fields = ('id', 'user')