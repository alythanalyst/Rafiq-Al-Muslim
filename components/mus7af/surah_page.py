#surah_page.py
import flet as ft
import json

class SurahPage(ft.Control): 
    def __init__(self, surah_index):
        super().__init__()
        self.surah_index = surah_index

    def build(self):
        try:
            with open(f"assets/surah/surah_{int(self.surah_index)}.json", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return ft.Text("Surah data not found.", color="red")

        verses = data["verse"]
        name = data["name"]

        verse_controls = [
            ft.Text(f"{num[6:]}: {ayah}", size=20, text_align=ft.TextAlign.RIGHT)
            for num, ayah in verses.items()
        ]

        return ft.Column(
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text(f"Surah: {name}", size=22, weight=ft.FontWeight.BOLD),
                *verse_controls
            ]
        )

    def _get_control_name(self):
        return f"surah_{self.surah_index}"
