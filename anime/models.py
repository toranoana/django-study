from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    season = models.IntegerField() # 1, 4, 7, 10
