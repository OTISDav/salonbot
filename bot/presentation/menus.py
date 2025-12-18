# Menu principal du bot
MAIN_MENU = {
    "1": "Prendre un rendez-vous",
    "2": "Voir les services",
    "3": "Horaires et localisation",
    "4": "Parler à un coiffeur"
}

# Fonctions pour renvoyer le menu en texte
def main_menu_text():
    return "📋 Menu principal :\n" + "\n".join([f"{k}. {v}" for k, v in MAIN_MENU.items()])
