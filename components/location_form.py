# components/location_form.py

import flet as ft
from services.location_manager import save_location

def LocationForm(on_submit):
    city_field = ft.TextField(label="City", width=200)
    country_field = ft.TextField(label="Country", width=200)

    def handle_click(e):
        city = city_field.value.strip()
        country = country_field.value.strip()
        if city and country:
            save_location(city, country)
            on_submit(city, country)

    return ft.Column([
        ft.Text("🌍 Set Your Location", size=18, weight=ft.FontWeight.BOLD),
        city_field,
        country_field,
        ft.ElevatedButton("Save Location & Refresh", on_click=handle_click),
    ])
