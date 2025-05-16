from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitsCreateAPIView,
    HabitsDestroyAPIView,
    HabitsListAPIView,
    HabitsRetrieveAPIView,
    HabitsUpdateAPIView,
)

app_name = HabitConfig.name

urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="habits-list"),
    path("habits/create/", HabitsCreateAPIView.as_view(), name="habits-create"),
    path(
        "habits/<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits-update"
    ),
    path("habits/<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habits-get"),
    path(
        "habits/<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits-delete"
    ),
]
