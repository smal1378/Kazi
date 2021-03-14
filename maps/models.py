from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Map(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete="Cascade")
    current_water = models.IntegerField(default=0)


class Part(models.Model):
    map = models.ForeignKey(Map, on_delete="Cascade")
    name = models.CharField(max_length=50)


class Col:
    size = models.FloatField()
    master = models.ForeignKey(Part, on_delete="Cascade")


class Row:
    master = models.ForeignKey(Part, on_delete="Cascade")
    size = models.FloatField()


class Watered:
    date = models.DateField()
    col = models.ForeignKey(Col, on_delete="Cascade")
    row = models.ForeignKey(Row, on_delete="Cascade")
    number = models.IntegerField()
