from rest_framework import viewsets
from todolist.api import serializers
from todolist import models
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()    