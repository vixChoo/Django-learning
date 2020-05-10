from django.db import models

# class for todo Item
class TodoItem(models.Model) :
    content = models.TextField()
