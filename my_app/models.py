from django.db import models

# Create your models here.
# create a person table with three column

class Person(models.Model):
    # class variables
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.name + " " + str(self.age) + " " + str(self.address)
