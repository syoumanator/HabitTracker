from rest_framework import generics

from habit.models import Habits
from habit.pagination import HabitPagination
from habit.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    """Список привычек"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitPagination

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Изменение привычки"""

    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habits.objects.all()
    permission_classes = (IsOwner,)
