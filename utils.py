import os
import random


def get_random_word():
    """Lee wordlist.txt y devuelve una palabra al azar."""
    ruta = os.path.join(os.path.dirname(__file__), "wordlist.txt")

    with open(ruta, "r", encoding="utf-8") as archivo:
        palabras = [
            linea.strip()
            for linea in archivo
            if linea.strip().isalpha()
        ]

    if not palabras:
        raise ValueError("wordlist.txt no tiene palabras válidas")

    return random.choice(palabras)
