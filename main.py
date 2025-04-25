#main.py
import flet as ft
import requests
from core.api import get_prayer_times
from components.prayer_card import create_prayer_card
from components.ayah_player import create_ayah_clickable
from components.prayer_times import display_prayer_times

user_location = {"city": "Cairo", "country": "Egypt"}

def check_internet_connection():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

# Main Page
def home_page(page: ft.Page):
    page.clean()
    page.title = "Rafiq Al-Muslim - Prayer Times"
    
    page.add(
        ft.Row([ 
            ft.Text("Today's Prayer Times 🕌", size=26, weight=ft.FontWeight.BOLD, expand=1),
            ft.IconButton(icon=ft.icons.LOCATION_PIN, tooltip="Settings", on_click=lambda e: page.go("/settings")),
            ft.ElevatedButton("Athkar", on_click=lambda _: page.go("/athkar")),
            ft.ElevatedButton("📖 Mus7af", on_click=lambda _: page.go("/quran"))

        ])
    )
    
    timings = get_prayer_times(city=user_location["city"], country=user_location["country"])

    for prayer, time in timings.items():
        if prayer not in ["Sunset", "Midnight"]:
            page.add(create_prayer_card(prayer, time))

# Settings Page
def settings_page(page: ft.Page):
    page.clean()
    page.title = "Settings"

    city_input = ft.TextField(label="City", value=user_location["city"])
    country_input = ft.TextField(label="Country", value=user_location["country"])

    def save_settings(e):
        user_location["city"] = city_input.value
        user_location["country"] = country_input.value
        page.go("/")  

    page.add(
        ft.Text("Change Location", size=26, weight=ft.FontWeight.BOLD),
        city_input,
        country_input,
        ft.ElevatedButton("Save", on_click=save_settings),
        ft.TextButton("Back to Home", on_click=lambda e: page.go("/"))
    )

# Main App
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    def route_change(route):
        if page.route == "/settings":
            settings_page(page)
        elif page.route == "/athkar":
            from components.athkar_page import athkar_page
            athkar_page(page)
        elif page.route == "/quran":
            from components.quran_page import quran_page
            quran_page(page)
        else:
            home_page(page)

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)
