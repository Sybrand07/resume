from django.contrib import admin
from .models import Ride

# Register your models here.
# Register the Ride model with a custom admin section called "Liftclub"
@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('pickup_location', 'destination', 'date_time')