from django.utils import timezone
from django.db import models


class Timeline(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        return self.name


class Event(models.Model):
    timeline = models.ForeignKey(Timeline, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.name
    
    def is_current(self):
        return self.start_date <= timezone.now() <= self.end_date
    
    def get_duration(self):
        return self.end_date - self.start_date