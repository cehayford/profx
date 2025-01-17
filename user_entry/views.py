from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from .serializers import MedialinksSerializer
from .models import MediaLinks

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
            serializer = MedialinksSerializer(instance=media_link, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except MediaLinks.DoesNotExist:
            return Response({'status':'Media link do not exist in the database...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)
