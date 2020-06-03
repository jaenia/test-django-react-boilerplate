from rest_framework import serializers

from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id', 'text', 'is_done')
        read_only_fields = ('id',)
