#components/prayer_times.py
import flet as ft
from core.api import get_prayer_times
from components.prayer_card import create_prayer_card

# Display the prayer times
def display_prayer_times(page: ft.Page, user_location):
    timings = get_prayer_times(city=user_location["city"], country=user_location["country"])

    for prayer, time in timings.items():
        if prayer not in ["Sunset", "Midnight"]:
            page.add(create_prayer_card(prayer, time))
