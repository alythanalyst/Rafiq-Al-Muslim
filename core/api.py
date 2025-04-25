# core/api.py
import requests
from datetime import datetime

def get_prayer_times(city="Cairo", country="Egypt", method=5):
    """
    Fetches prayer times for the current day from Aladhan API.
    """
    today = datetime.now().strftime("%d-%m-%Y")
    url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method={method}&date={today}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["data"]["timings"]
    except Exception as e:
        print("Error fetching prayer times:", e)
        return {}
