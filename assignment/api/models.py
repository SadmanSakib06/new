from django.db import models

# Create your models here.

size_choice = (
    ('Tiny','Tiny'),
    ('Small','Small'),
    ('Medium','Medium'),
    ('Large','Large')
)

friendliness_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)

trainability_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)

shedding_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)
exersize_choice = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5)
)

class Breed(models.Model):
    name = models.CharField(max_length=25)
    size = models.CharField(max_length=10, choices=size_choice)
    friendliness = models.IntegerField(choices=friendliness_choice)
    trainability = models.IntegerField(choices=trainability_choice)
    sheddingamount = models.IntegerField(choices=shedding_choice)
    exersizeneeds = models.IntegerField(choices=exersize_choice)

    def __str__(self):
        return self


gender_choice = (
    ('Male','Male'),
    ('Female','Female')
)

class Dog(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10,choices=gender_choice)
    color = models.CharField(max_length=10)
    food = models.CharField(max_length=20)
    toy = models.CharField(max_length=20)

    def __str__(self):
        return self


