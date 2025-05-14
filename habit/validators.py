from rest_framework.exceptions import ValidationError

list_commands = ["Исключить одновременный выбор связанной привычки и указания вознаграждения!",
                 "Время выполнения должно быть не больше 120 секунд!",
                 "В связанные привычки могут попадать только привычки с признаком приятной привычки!",
                 "У связанной привычки должен быть указан признак приятной привычки!",
                 "Нельзя выполнять привычку реже, чем 1 раз в 7 дней!"]


class AssociatedWithoutRewardValidator:
    """Исключить одновременный выбор связанной привычки и указания вознаграждения!"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, instance):
        if instance.get(self.field1) and instance.get(self.field2):
            raise ValidationError(list_commands[0])


class TimeToCompleteValidator:
    """Время выполнения должно быть не больше 120 секунд!"""
    duration = 120

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, instance):
        if instance.get(self.field1):
            if instance.get(self.field1) > self.duration:
                raise ValidationError(list_commands[1])


class PleasantHabitRelatedValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки!"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, instance):
        if instance.get(self.field1):
            if not instance.get(self.field2):
                raise ValidationError(list_commands[2])


class PleasantHabitWithoutReward:
    """У связанной привычки должен быть указан признак приятной привычки!"""

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __call__(self, instance):
        if instance.get(self.field1):
            if instance.get(self.field2) or instance.get(self.field3):
                raise ValidationError(list_commands[3])


class PeriodicityValidator:
    """Нельзя выполнять привычку реже, чем 1 раз в 7 дней!"""
    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, instance):
        periodicity = instance.get(self.field1)
        if periodicity:
            if periodicity > 7:
                raise ValidationError(list_commands[4])
