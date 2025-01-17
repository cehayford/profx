from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import MedialinksSerializer, UserinfoSerializer, SkillsSerializer
from .models import MediaLinks, userinfo, Skills, ProgLanguage, OtherLanguage, Tools, Databases, Frameworks
from .re_vert import *

# Create your views here.
class UserinfoView(APIView):
    def get(self, request):
        users = userinfo.objects.all()
        serializer = UserinfoSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = UserinfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User info created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class UpdateUserinfo(APIView):
    def put(self, request, pk):
        try:
            user = userinfo.objects.get(id=pk)
        except userinfo.DoesNotExist:
            return Response({'error': 'User not found'}, status=HTTP_404_NOT_FOUND)
        
        serializer = UserinfoSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User info updated successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SkillsView(APIView):
    def get(self, request):
        skills = Skills.objects.all()
        prog_languages = ProgLanguage.objects.all()
        other_languages = OtherLanguage.objects.all()
        tools = Tools.objects.all()
        databases = Databases.objects.all()
        frameworks = Frameworks.objects.all()

        skills_serializer = SkillsSerializer(skills, many=True)
        prog_languages_serializer = SkillsSerializer(prog_languages, many=True)
        other_languages_serializer = SkillsSerializer(other_languages, many=True)
        tools_serializer = SkillsSerializer(tools, many=True)
        databases_serializer = SkillsSerializer(databases, many=True)
        frameworks_serializer = SkillsSerializer(frameworks, many=True)

        return Response({
            'skills': skills_serializer.data,
            'prog_languages': prog_languages_serializer.data,
            'other_languages': other_languages_serializer.data,
            'tools': tools_serializer.data,
            'databases': databases_serializer.data,
            'frameworks': frameworks_serializer.data
        }, status=HTTP_200_OK)


class GetMediaLinks(APIView):
    def get(self, request):
        media_links = MediaLinks.objects.all()
        serializer = MedialinksSerializer(media_links, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CreateMediaLink(APIView):
    def post(self, request):
        serializer = MedialinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Media link created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UpdateMediaLink(APIView):
    def put(self, request, pk):
        try:
            media_link = MediaLinks.objects.get(id=pk)
        except MediaLinks.DoesNotExist:
            return Response({'error': 'Media link not found'}, status=HTTP_404_NOT_FOUND)
        
        serializer = MedialinksSerializer(media_link, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Media link updated successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)