from django.contrib import admin
from .domain.models import Client, Appointment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("phone", "state")
    readonly_fields = ("context",)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("client", "service", "barber", "date", "time", "status", "created_at")
    list_filter = ("status", "date")
    search_fields = ("client__phone", "service", "barber")
