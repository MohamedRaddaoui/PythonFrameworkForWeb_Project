from django.contrib import admin
from .models import *

from django.contrib import admin

# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('participant', 'conference', 'reservation_date')

admin.site.register(Participant)
admin.site.register(Reservation, ReservationAdmin)