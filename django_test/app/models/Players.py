import datetime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from app.models.Teams import Teams
from app.models.Positions import Positions

class Players(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    nickname=models.CharField(max_length=120)
    birthday=models.DateField(null=True,blank=True)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    salary = models.FloatField()
    contract_duration = models.IntegerField()
    team = models.ForeignKey(Teams, related_name='player', verbose_name='Team', on_delete=models.CASCADE)
    positions = models.ManyToManyField(Positions)
    country=models.CharField(max_length=50)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def age(self):
        return int((datetime.date.today() - self.birthday).days / 365.25)