from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from mixer.backend.django import mixer
from users.views import UserModelViewSet
from projects.models import Project
from users.models import User as CustomUser
from django.contrib.auth.models import User


class TestUserViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = mixer.blend(CustomUser)
        client = APIClient()
        response = client.put(f'/api/users/{user.uid}/', {'username': 'user_1', 'birthday_year': 1990})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestProjectViewSet(APITestCase):

    def test_edit_project_user(self):
        user = User.objects.create(username='user_1', first_name='qwe', password='user123456')
        project = Project.objects.create(name='project_1', rep_link='github.com')
        self.client.login(username='user_1', password='user123456')
        response = self.client.put(f'/api/projects/{project.id}/', {'name': 'project_1', 'rep_link': 'github.com'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)



