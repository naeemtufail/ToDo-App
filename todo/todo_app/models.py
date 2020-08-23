from django.db import models

class Todo(models.Model):
    date_added=models.DateTimeField()
    text=models.CharField(max_length=500)
def __str__(self):
    return (self.text)