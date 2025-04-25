# services/location_manager.py

import json
import os

PREF_FILE = "data/preferences.json"

def load_location():
    if os.path.exists(PREF_FILE):
        with open(PREF_FILE, "r") as file:
            data = json.load(file)
            return data.get("city", "Makkah"), data.get("country", "Saudi Arabia")
    return "Makkah", "Saudi Arabia"

def save_location(city, country):
    with open(PREF_FILE, "w") as file:
        json.dump({"city": city, "country": country}, file)
