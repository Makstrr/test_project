from django.db import models

class OriginalName(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self

class Director(models.Model):
    name = models.CharField(max_length=64, unique=True)

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Movie(models.Model):
    name = models.CharField(max_length=64)
    original_name = models.OneToOneField(OriginalName, null=True, blank=True, on_delete=models.SET_NULL, related_name='movie')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='movie')
#    directors = models.ManyToManyField(Director, related_name='movie')

class DirectorMovie(models.Model):
    movie_id = models.ForeignKey(Movie, related_name='directors', on_delete=models.DO_NOTHING)
    director_id = models.ForeignKey(Director, related_name='movies', on_delete=models.DO_NOTHING)