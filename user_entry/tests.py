from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MediaLinks, userinfo, ProgLanguage, OtherLanguage, Tools, Databases, Frameworks, Skills

class MediaLinksTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.media_link_data = {'email': 'http://example.com', 'x': 'http://example.com/x', 'linkedin': 'http://linkedin.com'}
        self.media_link = MediaLinks.objects.create(**self.media_link_data)

    def test_create_media_link(self):
        response = self.client.post('/media-links/create/', self.media_link_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_media_link(self):
        update_data = {'email': 'http://newexample.com'}
        response = self.client.put(f'/media-links/update/{self.media_link.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.media_link.refresh_from_db()
        self.assertEqual(self.media_link.email, 'http://newexample.com')

class UserinfoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {'name': 'John Doe', 'email': 'john@example.com', 'phone': '1234567890', 'description': 'Test user', 'date_of_birth': '1990-01-01'}
        self.user = userinfo.objects.create(**self.user_data)

    def test_create_userinfo(self):
        response = self.client.post('/userinfo/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SkillsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.language = ProgLanguage.objects.create(name='Python')
        self.other_language = OtherLanguage.objects.create(name='Spanish')
        self.tool = Tools.objects.create(name='Django')
        self.database = Databases.objects.create(name='PostgreSQL')
        self.framework = Frameworks.objects.create(name='React')
        self.skill_data = {
            'language': self.language.id,
            'other_language': self.other_language.id,
            'tool': self.tool.id,
            'database': self.database.id,
            'framework': self.framework.id
        }
        self.skill = Skills.objects.create(**self.skill_data)

    def test_create_skill(self):
        response = self.client.post('/skills/', self.skill_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
