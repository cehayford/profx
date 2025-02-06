from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Projects
from uuid import uuid4

class ProjectsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project_data = {
            'title': 'Test Project',
            'technology': 'Django',
            'hostlink': 'http://example.com',
            'github_link': 'http://github.com/example'
        }
        self.project = Projects.objects.create(**self.project_data)

    def test_create_project(self):
        response = self.client.post('/projects/create/', self.project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_project(self):
        update_data = {'title': 'Updated Project'}
        response = self.client.put(f'/projects/update/{self.project.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project.refresh_from_db()
        self.assertEqual(self.project.title, 'Updated Project')

    def test_delete_project(self):
        response = self.client.delete(f'/projects/delete/{self.project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Projects.objects.filter(id=self.project.id).exists())
