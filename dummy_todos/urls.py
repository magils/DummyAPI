from django.urls import path
from dummy_todos import views

urlpatterns = [
    path("todos", views.TodoList.as_view()),
    path("todos/<int:pk>", views.TodoDetail.as_view())
]