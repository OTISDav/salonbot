from bot.domain.states import State
from bot.presentation.menus import MAIN_MENU, main_menu_text
from bot.presentation.templates import services_message, SERVICES
from bot.services.appointment import create_appointment
from bot.domain.rules import validate_service, validate_date, validate_time
from bot.services.coiffeur_notify import notify_new_client, notify_appointment

GREETINGS = ["salut", "bonjour", "coucou", "hello"]

def handle_message(client, message):
    msg = message.strip().lower()

    # Salutations
    if msg in GREETINGS and client.state == State.START:
        client.state = State.MENU
        client.save()
        return "👋 Bonjour ! Je suis le bot du salon. Pour commencer, choisissez une option :\n" + main_menu_text()

    # Commande spéciale pour revenir au menu
    if msg in ["0", "menu", "quit"]:
        client.state = State.MENU
        client.context = {}
        client.save()
        return "🔄 Retour au menu principal.\n" + main_menu_text()

    # Demande du nom si nécessaire
    if client.state == State.ASK_NAME:
        client.name = msg.title()
        next_action = client.context.pop("next_action", None)
        client.save()

        if next_action == "1":
            client.state = State.SERVICE
            client.save()
            return services_message()
        elif next_action == "4":
            client.state = State.HUMAN
            client.save()
            notify_new_client(client)
            return "👤 Un coiffeur va vous répondre (simulation locale)."

    # Menu principal
    if client.state == State.MENU:
        # Vérifie si le nom est renseigné
        if msg in ["1", "4"] and not getattr(client, "name", None):
            client.state = State.ASK_NAME
            client.context["next_action"] = msg
            client.save()
            return "👋 Bonjour ! Quel est votre nom ?"

        if msg == "1":
            client.state = State.SERVICE
            client.save()
            return services_message()
        elif msg == "2":
            return services_message()
        elif msg == "3":
            return "🕒 Horaires : 8h-18h\n📍 Adresse : Rue du Salon, Lomé"
        elif msg == "4":
            client.state = State.HUMAN
            client.save()
            notify_new_client(client)
            return "👤 Un coiffeur va vous répondre (simulation locale)."
        else:
            return "❌ Choix invalide. " + main_menu_text()

    # Prise de service
    if client.state == State.SERVICE:
        if not validate_service(msg):
            return "❌ Service invalide. Veuillez choisir 1, 2, 3 ou 4, ou 0 pour retourner au menu."
        client.context["service"] = msg
        client.state = State.DATE
        client.save()
        return "📅 Entrez la date (YYYY-MM-DD)"

    # Prise de date
    if client.state == State.DATE:
        if not validate_date(msg):
            return "❌ Date invalide. Format attendu YYYY-MM-DD, ou 0 pour retourner au menu."
        client.context["date"] = msg
        client.state = State.TIME
        client.save()
        return "⏰ Entrez l’heure (HH:MM)"

    # Prise de l'heure
    if client.state == State.TIME:
        if not validate_time(msg):
            return "❌ Heure invalide. Format attendu HH:MM, ou 0 pour retourner au menu."
        client.context["time"] = msg

        service_id = client.context.get("service")
        service_name = SERVICES.get(service_id, "Service inconnu")
        client.context["service_name"] = service_name
        create_appointment(client)
        notify_appointment(client)
        client.state = State.START
        client.context = {}
        client.save()
        return "✅ Rendez-vous confirmé ! (simulation locale)"

    # Assistance humaine
    if client.state == State.HUMAN:
        return "👤 Un coiffeur va vous répondre sous peu."

    return "❓ Je n’ai pas compris."
