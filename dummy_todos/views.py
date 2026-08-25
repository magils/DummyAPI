from django.core.serializers import serialize
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

    # NOTE: This method is not going to persist data for non-admin users
    def post(self, request):
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"todo": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):

    def handle_update(self, request, pk, status_code=status.HTTP_201_CREATED):

        if not Todo.objects.filter(pk=pk).exists():
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"todo": serializer.data}, status=status_code)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo)
            return Response({"todo": serializer.data})
        except Todo.DoesNotExist:
            return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        return self.handle_update(request, pk)

    def patch(self, request, pk):
        return self.handle_update(request, pk)

    def delete(self, request, pk):
        return Response(status=status.HTTP_204_NO_CONTENT)