# /core/utils.py
import json
import os

def load_surah(index: str):
    path = f"assets/surah/surah_{int(index)}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
