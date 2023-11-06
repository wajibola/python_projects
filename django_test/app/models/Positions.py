from django.db import models
from django.contrib.postgres.fields import ArrayField

class Positions(models.Model):
    position = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=120)
    
    def __str__(self):
        return self.name