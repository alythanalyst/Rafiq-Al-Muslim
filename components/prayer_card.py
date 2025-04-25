# components/prayer_card.py
import flet as ft

def create_prayer_card(prayer_name, prayer_time):
    return ft.Card(
        content=ft.ListTile(
            title=ft.Text(prayer_name),
            subtitle=ft.Text(f"Time: {prayer_time}"),
            trailing=ft.Icon(ft.icons.NOTIFICATIONS_ACTIVE_OUTLINED),
        )
    )
