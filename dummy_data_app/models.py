from django.db import models

class News(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField()
    summary = models.TextField()
    content = models.TextField()
    category = models.CharField(max_length=512)
    author = models.CharField(max_length=1024)
    source = models.CharField(max_length=1024)
    url = models.URLField()
    country = models.CharField(max_length=512)
    is_featured = models.BooleanField(default=False)
    is_breaking = models.BooleanField(default=False)
    published_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)