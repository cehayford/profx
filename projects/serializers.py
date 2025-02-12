from rest_framework import serializers
from .models import Projects


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex_verbose')
    
    class Meta:
        model = Projects
        fields = '__all__'


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    title = serializers.CharField(max_length=100)
    message = serializers.CharField()
    phone = serializers.CharField(max_length=15, required=False)
    