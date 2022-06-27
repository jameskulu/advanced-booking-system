from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):
    slots = models.PositiveBigIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return f'{self.location} -> {self.date} -> {self.time}'
    
    class Meta:
        unique_together = ('location', 'date', 'time')