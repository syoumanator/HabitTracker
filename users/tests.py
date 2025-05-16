from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client.force_authenticate(user=self.user)

    def test_user_register(self):
        """Создание пользователя"""
        data = {"email": "test@test.com", "password": "123456789"}
        response = self.client.post("/users/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_update(self):
        """Обновление пользователя"""

        data = {"first_name": "User", "last_name": "Test"}
        response = self.client.patch(f"/users/{self.user.pk}/update/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        """Просмотр пользователя"""
        response = self.client.get(f"/users/{self.user.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_delete(self):
        """Удаление пользователя"""
        response = self.client.delete(f"/users/{self.user.pk}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

