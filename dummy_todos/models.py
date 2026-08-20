from django.db import models

class User(models.Model):
    name = None
    last_name = None
    email = None

class Todo(models.Model):
    title = None
    description = None
    status = None
    user = None
    date_updated = None
    date_completed = None
    date_created = None
    priority = None
