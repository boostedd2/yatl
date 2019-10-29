from django.db import models
import datetime

class Todo(models.Model):

    title = models.CharField(max_length=200)

    body = models.TextField()
    
    start_date = models.DateField(default=datetime.date.today)

    end_date = models.DateField(null=True, blank=True)

    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.title