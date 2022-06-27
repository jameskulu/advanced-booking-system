from django.contrib import admin
from .models import Location, Appointment

admin.site.register([Location, Appointment])
