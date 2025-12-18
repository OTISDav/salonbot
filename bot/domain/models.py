from django.db import models

class Client(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=True)   # nom du client
    state = models.CharField(max_length=50, default="START")
    context = models.JSONField(default=dict)

    def __str__(self):
        return self.phone


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    barber = models.CharField(max_length=100, blank=True)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="CONFIRMED")
    created_at = models.DateTimeField(auto_now_add=True)
