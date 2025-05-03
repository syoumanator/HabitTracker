from django.contrib import admin

from habit.models import Habits


@admin.register(Habits)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "act",
        "pleasant_habit",
        "related_habit",
        "periodicity",
        "prize",
        "lead_time",
        "is_published",
    )
