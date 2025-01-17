from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import ProgLanguageSerializer, OtherLanguageSerializer, ToolsSerializer, DatabasesSerializer, FrameworksSerializer, SkillsSerializer
from .models import ProgLanguage, OtherLanguage, Tools, Databases, Frameworks


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