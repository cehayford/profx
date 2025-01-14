from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.response import Response
from .serializers import ProjectSerializer
from projects.models import Projects


class getProjectsView(APIView):
    def get(self, request):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class createProjectView(APIView):
    def post(self, request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e: 
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)


class updateProjectView(APIView):
    def put(self, request, pk):
        try:
            project = Projects.objects.get(id=pk)
            serializer = ProjectSerializer(instance=project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            project = Projects.objects.get(id=pk)
            serializer = ProjectSerializer(instance=project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error': str(e)}, status=HTTP_404_NOT_FOUND)
        

class deleteProjectView(APIView):
    def delete(self, request, pk):
        try:
            project = Projects.objects.get(id=pk)
            project.delete()
            return Response({'message': 'Project information have deleted successfully'}, status=HTTP_200_OK)
        except Projects.DoesNotExist:
            return Response({'status':'Product do not exist in the cart...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)