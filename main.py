def get_valid_letter(guessed_letters):
    """Solicita una letra válida que no haya sido intentada anteriormente."""
    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida. Ingresa una sola letra.")
        elif letter in guessed_letters:
            print("Ya intentaste esa letra. Prueba con otra.")
        else:
            return letter