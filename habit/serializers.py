from rest_framework import serializers
from habit.models import Habits


class HabitsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habits
        fields = "__all__"
        # validators =

