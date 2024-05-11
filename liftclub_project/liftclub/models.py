from django.db import models

class Ride(models.Model):
    # Define fields for the Ride model
    pickup_location = models.CharField(max_length=100)  # Location where the user wants to be picked up
    destination = models.CharField(max_length=100)      # Destination where the user wants to go
    date_time = models.DateTimeField()                  # Date and time of the ride

    # String representation of the Ride object
    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.destination} on {self.date_time}"
