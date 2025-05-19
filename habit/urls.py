from django.urls import path

from habit.apps import HabitConfig
from habit.views import (
    HabitsCreateAPIView,
    HabitsDestroyAPIView,
    HabitsListAPIView,
    HabitsRetrieveAPIView,
    HabitsUpdateAPIView,
    PublishedHabitsListAPIView,
)

app_name = HabitConfig.name

urlpatterns = [
    path("", HabitsListAPIView.as_view(), name="habits-list"),
    path("create/", HabitsCreateAPIView.as_view(), name="habits-create"),
    path("<int:pk>/update/", HabitsUpdateAPIView.as_view(), name="habits-update"),
    path("<int:pk>/", HabitsRetrieveAPIView.as_view(), name="habits-get"),
    path("<int:pk>/delete/", HabitsDestroyAPIView.as_view(), name="habits-delete"),
    path("public/list/", PublishedHabitsListAPIView.as_view(), name="public-habits"),
]
