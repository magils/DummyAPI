from datetime import datetime

from django.db import models
from enum import Enum

class TodoStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

    @classmethod
    def choices(cls):
        return [(s.value, s.name.replace("_", " ").title()) for s in cls]

class TodoPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"

    @classmethod
    def choices(cls):
        return [(p.value, p.name.title()) for p in cls]

class User(models.Model):
    name = models.TextField(max_length=512, null=False)
    last_name = models.TextField(max_length=512, null=False)
    email = models.EmailField(null=False)

class Todo(models.Model):
    title = models.CharField(max_length=1024, null=False)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=TodoStatus.choices(), default=TodoStatus.NOT_STARTED, null=False)
    priority = models.CharField(max_length=20, choices=TodoPriority.choices(), default=TodoPriority.NORMAL, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)
    date_completed = models.DateTimeField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

