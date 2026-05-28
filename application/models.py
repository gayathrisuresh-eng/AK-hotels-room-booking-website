from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    room_number=models.IntegerField()
    room_type=models.CharField(max_length=100)
    price=models.IntegerField()
    available=models.BooleanField(default=True)

    def __str__(self):
        return str(self.room_number)

class Booking(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   room=models.ForeignKey(Room,on_delete=models.CASCADE)
   check_in=models.DateField()
   check_out=models.DateField()