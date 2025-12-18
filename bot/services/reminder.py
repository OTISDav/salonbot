from datetime import datetime, timedelta
from bot.domain.models import Appointment

def get_upcoming_appointments():
    now = datetime.now()
    reminders = []
    for appt in Appointment.objects.filter(status="CONFIRMED"):
        appt_datetime = datetime.combine(appt.date, appt.time)
        if timedelta(0) <= appt_datetime - now <= timedelta(hours=1):
            reminders.append(appt)
        elif timedelta(0) <= appt_datetime - now <= timedelta(days=1):
            reminders.append(appt)
    return reminders

def send_reminder(appt, send_func):
    message = f"📌 Rappel : votre RDV pour {appt.service} est prévu le {appt.date} à {appt.time}"
    send_func(appt.client.phone, message)
