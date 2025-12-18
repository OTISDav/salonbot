import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bot.domain.models import Client
from bot.services.conversation import handle_message

@csrf_exempt
def whatsapp_webhook(request):
    if request.method != "POST":
        return JsonResponse({"error": "Méthode non autorisée"}, status=405)

    data = json.loads(request.body)
    phone = data.get("from")
    message = data.get("message")

    if not phone or not message:
        return JsonResponse({"error": "Données invalides"}, status=400)

    client, _ = Client.objects.get_or_create(phone=phone)
    reply = handle_message(client, message)

    return JsonResponse({"reply": reply})
