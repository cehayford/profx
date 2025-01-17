from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.core.mail import send_mail
from .serializers import ProjectSerializer, ContactFormSerializer
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


class contactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            title = serializer.validated_data['title']
            phone = serializer.validated_data['phone']
            message = serializer.validated_data['message']
            try:
                send_mail(
                    f"Message from {name}",
                    title,
                    message,
                    email,
                    ['your_email@example.com'],
                    phone,
                    fail_silently=False,
                )
                return Response({'message': 'Email sent successfully'}, status=HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)