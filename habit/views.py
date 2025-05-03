from rest_framework import generics



class HabitsCreateAPIView(generics.CreateAPIView):
    pass


class HabitsListAPIView(generics.ListAPIView):
    pass


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    pass


class HabitsUpdateAPIView(generics.UpdateAPIView):
    pass

class HabitsDestroyAPIView(generics.DestroyAPIView):
    pass