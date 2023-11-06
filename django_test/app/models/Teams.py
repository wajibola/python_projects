from django.db import models
from django.contrib.postgres.fields import ArrayField

class Teams(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=50)
    date_of_creation = models.DateField()
    website=models.CharField(null=True, blank=True, max_length=120)

    def __str__(self):
        return self.name