#core/quran_reader.py
import json
import os

SURAH_DIR = "assets/surah"
SURAH_METADATA_PATH = "assets/surah.json"
JUZ_METADATA_PATH = "assets/juz.json"

def load_surah_metadata():
    with open(SURAH_METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_juz_metadata():
    with open(JUZ_METADATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def load_juz(juz_index):

    path = os.path.join("assets/juz", f"juz_{str(juz_index).zfill(2)}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_surah(index):
    path = os.path.join(SURAH_DIR, f"surah_{int(index)}.json") 
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def load_audio_for_verse(reciter_id, surah_index, ayah_index):
    # Construct the URL for the audio
    audio_url = f"https://everyayah.com/data/{reciter_id}/{str(surah_index).zfill(3)}{str(ayah_index).zfill(3)}.mp3"
    return audio_url
