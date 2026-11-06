import random
from game import HangmanGame

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
    # Cargar palabras desde wordlist.txt
    try:
        with open("wordlist.txt", "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        words = ["python", "programacion", "ahorcado", "desarrollo", "github"]

    # Seleccionar palabra aleatoria
    word = random.choice(words)
    game = HangmanGame(word)

    print("========================================")
    print("   ¡BIENVENIDO AL JUEGO DEL AHORCADO!   ")
    print("========================================")

    # Bucle principal del juego
    while game.errors < game.max_errors:
        print("\n----------------------------------------")
        # Mostrar letras intentadas hasta el momento
        print(f"Letras intentadas: {', '.join(game.guessed_letters) if game.guessed_letters else 'Ninguna'}")
        
        print("Progreso actual:")
        current_progress = game.display_progress()
        
        # Mostrar intentos incorrectos restantes (max_errors - errors)
        intentos_restantes = game.max_errors - game.errors
        print(f"Intentos incorrectos restantes: {intentos_restantes} / {game.max_errors}")
        
        # Verificar condición de victoria
        if "_" not in current_progress:
            print(f"\n¡Felicidades! Has ganado. La palabra era: {game.word}")
            break
            
        # Obtener letra válida del usuario
        letter = get_valid_letter(game.guessed_letters)
        
        # Procesar intento
        success = game.process_guess(letter)
        if success:
            print(f"¡Bien hecho! '{letter}' está en la palabra.")
        else:
            print(f"Letra incorrecta. Te quedan {game.max_errors - game.errors} intentos.")
            
        # Verificar condición de derrota
        if game.errors >= game.max_errors:
            print("\n----------------------------------------")
            print(f"¡Game Over! Te has quedado sin intentos. La palabra era: {game.word}")
            print("----------------------------------------")
            break

if __name__ == "__main__":
    main()
