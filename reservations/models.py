from django.db import models

class Reservation(models.Model):
    from passengers.models import Passenger
    passengerid = models.ForeignKey(Passenger, related_name='reservations',on_delete=models.PROTECT)
    status= models.BooleanField(default='Created')
    created_at=models.DateField(auto_now_add=True)
    reservation_date=models.DateField()

    def __str__(self):
        return f"{self.passenger.frist_name} - {self.status}"
