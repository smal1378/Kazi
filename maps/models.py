from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Map(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    current_water = models.IntegerField(default=0)
    time_created = models.DateTimeField()
    notes = models.TextField()
    s = models.FloatField(default=0)
    rank = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return self.name


class Part(models.Model):
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    x = models.IntegerField()
    y = models.IntegerField()
    s = models.FloatField(default=0)

    def __str__(self):
        return self.map.name + ": " + self.name


class Col(models.Model):
    size = models.FloatField()
    master = models.ForeignKey(Part, on_delete=models.CASCADE)

    def __str__(self):
        return self.master.map.name + ": " + self.master.name + " - Column " + str(self.pk)


class Row(models.Model):
    master = models.ForeignKey(Part, on_delete=models.CASCADE)
    size = models.FloatField()

    def __str__(self):
        return self.master.map.name + ": " + self.master.name + " - Row " + str(self.pk)


class Watered(models.Model):
    date = models.DateField()
    col = models.ForeignKey(Col, on_delete=models.CASCADE)
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    number = models.IntegerField()
