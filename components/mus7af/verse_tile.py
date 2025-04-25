#verse_tile.py
import flet as ft

class VerseTile(ft.Container):
    def __init__(self, index, text):
        super().__init__(
            padding=10,
            content=ft.Text(f"{text}", size=20, text_align="right"),
            border_radius=12,
            bgcolor="#1c1c1e"
        )
