from datetime import datetime

SERVICES = {
    "1": {"name": "Coupe homme", "price": 2000},
    "2": {"name": "Coupe femme", "price": 3000},
    "3": {"name": "Tresses", "price": 5000},
    "4": {"name": "Locks", "price": 7000},
}

BARBERS = ["Ali", "Moussa", "Koffi"]

def validate_service(service_id):
    return service_id in SERVICES

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_time(time_text):
    try:
        datetime.strptime(time_text, "%H:%M")
        return True
    except ValueError:
        return False
