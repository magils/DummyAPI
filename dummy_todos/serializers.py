from rest_framework import serializers
from dummy_todos.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("user",) # Exclude user field temporarily