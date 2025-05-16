from rest_framework import serializers

from habit.models import Habits

from .validators import (
    AssociatedWithoutRewardValidator,
    PeriodicityValidator,
    PleasantHabitRelatedValidator,
    PleasantHabitWithoutReward,
    TimeToCompleteValidator,
)


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = "__all__"
        validators = [
            PleasantHabitWithoutReward(
                field1="pleasant_habit", field2="prize", field3="related_habit"
            ),
            PleasantHabitRelatedValidator(
                field1="related_habit", field2="pleasant_habit"
            ),
            AssociatedWithoutRewardValidator(field1="related_habit", field2="prize"),
            TimeToCompleteValidator(field1="lead_time"),
            PeriodicityValidator(field1="periodicity"),
        ]
