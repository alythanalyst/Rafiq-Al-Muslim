#components/ayah_player.py
import flet as ft
import webbrowser

# Helper function to play audio
def play_audio(ayah_audio_url: str):
    if check_internet_connection():
        # Simulate playing the audio (you can replace with actual audio player logic)
        webbrowser.open(ayah_audio_url)
    else:
        print("No internet connection, cannot play audio.")

# Component to display Ayah and make it clickable
def create_ayah_clickable(ayah_text: str, ayah_audio_url: str):
    def on_click(e):
        play_audio(ayah_audio_url)

    return ft.ListTile(
        title=ft.Text(ayah_text),
        on_click=on_click,
        trailing=ft.Icon(ft.icons.PLAY_ARROW),
    )
