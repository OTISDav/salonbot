from bot.domain.models import Appointment

def create_appointment(client):
    Appointment.objects.create(
        client=client,
        service=client.context.get("service_name"),
        date=client.context.get("date"),
        time=client.context.get("time"),
    )
