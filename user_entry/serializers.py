from rest_framework import serializers
from .models import MediaLinks

class MedialinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaLinks
        fields = '__all__'


