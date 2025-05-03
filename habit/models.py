from django.db import models
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user",
        help_text="Создатель привычки",
        **NULLABLE
    )
    place = models.CharField(
        max_length=100,
        verbose_name="place",
        help_text="Место, в котором необходимо выполнять привычку",
    )
    time = models.TimeField(
        verbose_name="time", help_text="Время, когда необходимо выполнять привычку"
    )
    act = models.CharField(
        max_length=120,
        verbose_name="act",
        help_text="Действие, которое представляет собой привычка",
    )
    pleasant_habit = models.BooleanField(
        default=True,
        verbose_name="pleasant_habit",
        help_text="Привычка, которую можно привязать к выполнению полезной привычки",
    )
    related_habit = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="related_habit", **NULLABLE
    )
    periodicity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="periodicity",
        help_text="Периодичность выполнения привычки",
    )
    prize = models.CharField(
        max_length=100, verbose_name="prize", help_text="Награда после выполнения"
    )
    lead_time = models.PositiveSmallIntegerField(
        max_length=100, verbose_name="lead_time", help_text="Время на выполнение"
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Публикация в общий доступ"
    )

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
