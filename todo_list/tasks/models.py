from django.db import models

# Create your models here
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

