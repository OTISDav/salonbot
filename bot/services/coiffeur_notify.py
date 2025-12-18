from bot.infrastructure.whatsapp import send_whatsapp_message
from bot.presentation.templates import SERVICES



COIFFEUR_NUMBER = "+22801753075"  # Numéro WhatsApp du coiffeur

def notify_new_client(client, message=None):
    """
    Envoie au coiffeur le contact et le message du client
    """
    text = f"📩 Nouveau client souhaite parler à un coiffeur.\n"
    text += f"Nom : {client.name}\nTéléphone : {client.phone}\n"
    if message:
        text += f"Message : {message}"
    send_whatsapp_message(to=COIFFEUR_NUMBER, message=text)

def notify_appointment(client):
    """
    Envoie au coiffeur un nouveau rendez-vous confirmé
    """
    service_id = client.context.get("service")
    service_name = SERVICES.get(service_id, "Service inconnu")

    text = (
        f"📅 Nouveau rendez-vous !\n"
        f"Client : {client.name}\n"
        f"Téléphone : {client.phone}\n"
        f"Service : {service_name}\n"
        f"Date : {client.context.get('date')}\n"
        f"Heure : {client.context.get('time')}"
    )
    send_whatsapp_message(to=COIFFEUR_NUMBER, message=text)
