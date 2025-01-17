from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import MedialinksSerializer, UserinfoSerializer, SkillsSerializer
from .models import MediaLinks, userinfo, Skills
from re_vert import *

# Create your views here.
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



class SkillsView(APIView):
    def get(self, request):
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = SkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Skill created successfully'}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
