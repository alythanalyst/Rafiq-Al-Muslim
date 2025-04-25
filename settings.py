#settings.py
import flet as ft

def settings_page(page: ft.Page):
    page.title = "Settings"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO

    # Clear the page before adding content
    page.clear()

    # UI header
    page.add(ft.Text("Change Location", size=28, weight=ft.FontWeight.BOLD))

    # City and Country Input Fields
    city_input = ft.TextField(label="City", autofocus=True)
    country_input = ft.TextField(label="Country")

    # Button to save settings
    save_button = ft.ElevatedButton("Save", on_click=lambda e: save_settings(city_input, country_input, page))

    # Layout for inputs and button
    page.add(city_input, country_input, save_button)

def save_settings(city_input, country_input, page):
    city = city_input.value
    country = country_input.value

    # Save the values (you can store them in a file or in memory)
    print(f"Location saved: {city}, {country}")
    
    # After saving, navigate back to the main page
    page.go("/")
