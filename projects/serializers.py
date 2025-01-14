from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex_verbose')
    
    class Meta:
        model = Project
        fields = '__all__'