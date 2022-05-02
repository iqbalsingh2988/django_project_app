from django.db import models

# Create your models here.
class Species(models.Model):
   name = models.CharField(max_length=100)
   classification = models.CharField(max_length=100)
   language = models.CharField(max_length=100)


class Person(models.Model):
   name = models.CharField(max_length=100)
   birth_year = models.CharField(max_length=10)
   eye_color = models.CharField(max_length=10)
   species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)

class Task(models.Model):
    title = models.CharField(max_length = 200)
    completed = models.BooleanField(default = False, blank = True, null = True)

    def __str__(self):
        return self.title