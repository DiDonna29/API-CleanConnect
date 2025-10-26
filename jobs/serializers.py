# jobs/serializers.py
from rest_framework import serializers
from .models import Job, Application
from users.serializers import UserSerializer 

class JobSerializer(serializers.ModelSerializer):
    host_info = UserSerializer(source='host', read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ('id', 'host', 'status', 'created_at', 'updated_at')

    def create(self, validated_data):
        # Asigna el usuario autenticado como host
        validated_data['host'] = self.context['request'].user
        return super().create(validated_data)

class ApplicationSerializer(serializers.ModelSerializer):
    cleaner_info = UserSerializer(source='cleaner', read_only=True)

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('id', 'cleaner', 'status', 'created_at')

    def create(self, validated_data):
        # Asigna el usuario autenticado como cleaner
        validated_data['cleaner'] = self.context['request'].user
        return super().create(validated_data)