from django.db import models


class Anime(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    season = models.IntegerField() # 1, 4, 7, 10


class CV(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    sex = models.BooleanField()
    agency = models.CharField(max_length=50)
    official_url = models.CharField(max_length=255)


class AnimeCV(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.DO_NOTHING)
    cv = models.ForeignKey(CV, on_delete=models.DO_NOTHING)
