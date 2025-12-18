# Services proposés
SERVICES = {
    "1": "💇‍♂️ Coupe homme – 2000 FCFA",
    "2": "💇‍♀️ Coupe femme – 3000 FCFA",
    "3": "🌀 Tresses – 5000 FCFA",
    "4": "💆 Locks – 7000 FCFA"
}

def services_message():
    return "💇‍♀️ Nos services :\n" + "\n".join([f"{k}. {v}" for k, v in SERVICES.items()])
