from django.db import models

# Create your models here.
class RecommendedMovie(models.Model):
  title = models.CharField(max_length=100)
  listed_in = models.CharField(max_length=100)
  director = models.CharField(max_length=25)
  release_year = models.IntegerField()
  type = models.CharField(max_length=10)
  description = models.CharField(max_length=500)
  cast = models.CharField(max_length=200)

class SearchMovie(models.Model):
  title = models.CharField(max_length=100)
  release_year = models.IntegerField()
  cast = models.CharField(max_length=100)
  index = models.IntegerField()
