from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import *
from .models import MediaLinks, userinfo, Skills, ProgLanguage, OtherLanguage, Tools, Databases, Frameworks

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

class ProgLanguageView(APIView):
    def get(self, request):
        languages = ProgLanguage.objects.all()
        serializer = ProgLanguageSerializer(languages, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ProgLanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Programming language created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class OtherLanguageView(APIView):
    def get(self, request):
        languages = OtherLanguage.objects.all()
        serializer = OtherLanguageSerializer(languages, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = OtherLanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Other language created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ToolsView(APIView):
    def get(self, request):
        tools = Tools.objects.all()
        serializer = ToolsSerializer(tools, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ToolsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tool created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class DatabasesView(APIView):
    def get(self, request):
        databases = Databases.objects.all()
        serializer = DatabasesSerializer(databases, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = DatabasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Database created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class FrameworksView(APIView):
    def get(self, request):
        frameworks = Frameworks.objects.all()
        serializer = FrameworksSerializer(frameworks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = FrameworksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Framework created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

class SkillsView(APIView):
    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


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