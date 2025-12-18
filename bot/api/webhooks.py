import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bot.domain.models import Client
from bot.services.conversation import handle_message

VERIFY_TOKEN = "test1"  # EXACTEMENT le même que dans Meta

@csrf_exempt
def whatsapp_webhook(request):

    # 🔐 ÉTAPE 1 — Vérification Meta (GET)
    if request.method == "GET":
        mode = request.GET.get("hub.mode")
        token = request.GET.get("hub.verify_token")
        challenge = request.GET.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            return HttpResponse(challenge, content_type="text/plain")

        return HttpResponse("Forbidden", status=403)

    # 📩 ÉTAPE 2 — Messages WhatsApp (POST)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON invalide"}, status=400)

        # ⚠️ WhatsApp Cloud API structure réelle
        entry = data.get("entry", [{}])[0]
        changes = entry.get("changes", [{}])[0]
        value = changes.get("value", {})

        messages = value.get("messages")
        if not messages:
            return JsonResponse({"status": "no message"})

        msg = messages[0]
        phone = msg.get("from")
        text = msg.get("text", {}).get("body")

        if not phone or not text:
            return JsonResponse({"error": "Message invalide"}, status=400)

        client, _ = Client.objects.get_or_create(phone=phone)
        reply = handle_message(client, text)

        return JsonResponse({"reply": reply})

    return HttpResponse("Method not allowed", status=405)
