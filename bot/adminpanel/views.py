from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bot.domain.models import Appointment, Client

# @login_required
def dashboard(request):
    appointments = Appointment.objects.all().order_by("-date", "-time")
    clients = Client.objects.all()
    return render(request, "adminpanel/dashboard.html", {"appointments": appointments, "clients": clients})
