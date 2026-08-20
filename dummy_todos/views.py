from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from dummy_todos.models import Todo
from dummy_todos.serializers import TodoSerializer

class TodoList(APIView):

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response({"todos": serializer.data})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"todo": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors})

class TodoDetail(APIView):
    pass