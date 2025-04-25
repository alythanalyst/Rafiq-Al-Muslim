#components/quran_page.py
import pygame
import flet as ft
import requests
import io
import json
from core.quran_reader import load_surah_metadata, load_surah


pygame.mixer.init()


RECITERS_PATH = "assets/reciters.json"

def load_reciters():
    with open(RECITERS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {k: v for k, v in data.items() if k != "ayahCount"}

reciters = load_reciters()


def generate_audio_url(surah_index, verse_index, reciter_id):
    return f"https://everyayah.com/data/{reciter_id}/{int(surah_index):03}{int(verse_index):03}.mp3"



def play_audio_for_verse(surah_index, verse_index, reciter_id, verses=None):
    audio_url = generate_audio_url(surah_index, verse_index, reciter_id)
    print("Generated URL:", audio_url)
    try:
        response = requests.get(audio_url)
        if response.status_code == 200:
            audio_data = io.BytesIO(response.content)
            pygame.mixer.music.load(audio_data)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(2)

            if verses:
                keys = list(verses.keys())
                current_key = f"verse_{verse_index}"
                if current_key in keys:
                    idx = keys.index(current_key)
                    if idx + 1 < len(keys):
                        next_verse_key = keys[idx + 1]
                        next_index = int(next_verse_key.split('_')[1])
                        play_audio_for_verse(surah_index, next_index, reciter_id, verses)
        else:
            print("Failed to fetch audio.")
    except Exception as e:
        print("Error playing audio:", str(e))


def parse_verse_and_play_audio(surah_index, verse_key, reciter_id, auto_continue, verses):
    verse_index = int(verse_key.split('_')[1])
    play_audio_for_verse(surah_index, verse_index, reciter_id, verses if auto_continue else None)


def quran_page(page: ft.Page):
    page.clean()
    page.title = "Mus7af Reader \ud83d\udcd6"
    page.rtl = True
    surahs = load_surah_metadata()

    def open_surah(e, index):
        page.clean()
        surah_data = load_surah(index)
        verses = surah_data["verse"]

        page.title = f"{surah_data['name']} - Surah"
        page.add(ft.Text(f"سورة {surah['titleAr']} {surah_data['name']}", size=24, weight=ft.FontWeight.BOLD))

        reciter_ref = ft.Ref[ft.Dropdown]()
        auto_ref = ft.Ref[ft.Switch]()

        page.add(ft.Row([
            ft.Text("تفضيلات القارئ", size=18, weight=ft.FontWeight.BOLD)
        ]))

        page.add(
            ft.Dropdown(
                ref=reciter_ref,
                label="أختر القارئ",
                hint_text="Select Reciter",
                value="Abdul_Basit_Murattal_64kbps",
                options=[
                    ft.dropdown.Option(text=v["name"], key=v["subfolder"]) for v in reciters.values()
                ]
            )
        )

        page.add(ft.Switch(ref=auto_ref, label="Auto Continue", value=True))

        for verse_key, verse_text in verses.items():
            page.add(
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"آيه رقم {verse_key.split('_')[1]}", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(verse_text, size=20),
                        ft.ElevatedButton(
                            "Play Audio",
                            on_click=lambda e, s=index, v=verse_key: parse_verse_and_play_audio(
                                s,
                                v,
                                reciter_ref.current.value,
                                auto_ref.current.value,
                                verses
                            )
                        )
                    ])
                )
            )

        page.add(ft.TextButton("\u2190 Back to Surahs", on_click=lambda e: quran_page(page)))

    for surah in surahs:
        page.add(
            ft.ElevatedButton(
                f"{surah['index']}. {surah['titleAr']} ({surah['title']})",
                on_click=lambda e, idx=surah["index"]: open_surah(e, idx)
            )
        )
