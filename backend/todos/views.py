from rest_framework import viewsets
from todos import serializers
from todos.models import Todo


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = serializers.TodoSerializer
