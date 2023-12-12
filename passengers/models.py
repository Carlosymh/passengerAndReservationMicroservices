from django.db import models


class Passenger(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)


    def __str__(self):
        f"{self.first_name} - {self.Last_name}"

