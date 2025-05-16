from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habits
from users.models import User


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place="place",
            time="00:00",
            act="act",
            prize="prize",
            lead_time=120,
        )

    def test_habit_create(self):
        """Создание привычки"""
        data = {
            "place": "place",
            "time": "00:00",
            "act": "act",
            "prize": "prize",
            "lead_time": 120,
        }
        response = self.client.post("/habits/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_update(self):
        """Обновление привычки"""

        data = {
            "place": "new_place",
            "time": "07:07",
            "act": "act",
            "prize": "prize",
            "periodicity": 2,
        }
        response = self.client.patch(f"/habits/{self.habit.pk}/update/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_detail(self):
        """Просмотр привычки"""
        response = self.client.get(f"/habits/{self.habit.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_delete(self):
        """Удаление привычки"""
        response = self.client.delete(f"/habits/{self.habit.pk}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_habits(self):
        response = self.client.get("/habits/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
