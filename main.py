from game import HangmanGame
from utils import get_random_word


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


def main():
    # Seleccionar palabra aleatoria con la función de la Tarea 1
    word = get_random_word()
    game = HangmanGame(word)

    # Lista con todas las letras intentadas (acertadas e incorrectas)
    tried_letters = []

    print("========================================")
    print("   ¡BIENVENIDO AL JUEGO DEL AHORCADO!   ")
    print("========================================")

    # Bucle principal del juego
    while not game.is_lost():
        print("\n----------------------------------------")
        # Mostrar todas las letras intentadas hasta el momento
        print(f"Letras intentadas: {', '.join(tried_letters) if tried_letters else 'Ninguna'}")

        print("Progreso actual:")
        game.display_progress()

        # Mostrar intentos incorrectos restantes
        intentos_restantes = game.max_errors - game.errors
        print(f"Intentos incorrectos restantes: {intentos_restantes} / {game.max_errors}")

        # Verificar condición de victoria (Tarea 7: ignora espacios y signos)
        if game.is_won():
            print(f"\n¡Felicidades! Has ganado. La palabra era: {game.word}")
            break

        # Obtener letra válida que no se haya intentado antes
        letter = get_valid_letter(tried_letters)
        tried_letters.append(letter)

        # Procesar intento
        success = game.process_guess(letter)
        if success:
            print(f"¡Bien hecho! '{letter}' está en la palabra.")
        else:
            print(f"Letra incorrecta. Te quedan {game.max_errors - game.errors} intentos.")

        # Verificar condición de derrota
        if game.is_lost():
            print("\n----------------------------------------")
            print(f"¡Game Over! Te has quedado sin intentos. La palabra era: {game.word}")
            print("----------------------------------------")
            break


def ask_play_again():
    """Pregunta si el jugador quiere jugar otra partida."""
    while True:
        answer = input("\n¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if answer in ("s", "si", "sí"):
            return True
        if answer in ("n", "no"):
            return False
        print("Respuesta no válida. Escribe s o n.")


if __name__ == "__main__":
    while True:
        main()
        if not ask_play_again():
            print("¡Gracias por jugar!")
            break
            