from django.db import models


class Player(models.Model):
    position = models.IntegerField()
    name = models.CharField(max_length=100)
    result = models.IntegerField()
    result_race = models.TimeField()

    def __str__(self):
        return self.name
