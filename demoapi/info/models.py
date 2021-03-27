from django.db import models

# Create your models here.
class data(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.firstname