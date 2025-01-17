from rest_framework import serializers
from .models import MediaLinks, userinfo, ProgLanguage, OtherLanguage, Tools, Databases, Frameworks, Skills

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = userinfo
        fields = '__all__'
        depth = 1

class ProgLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgLanguage
        fields = '__all__'
        depth = 1

class OtherLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherLanguage
        fields = '__all__'
        depth = 1

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tools
        fields = '__all__'
        depth = 1

class DatabasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Databases
        fields = '__all__'
        depth = 1

class FrameworksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frameworks
        fields = '__all__'
        depth = 1

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
        depth = 1

class MedialinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLinks
        fields = '__all__'
        depth = 1
