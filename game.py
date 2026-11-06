class HangmanGame:
    """Guarda el estado de una partida del ahorcado."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra la palabra con las letras adivinadas y guiones bajos."""
        progress = []
        for letter in self.word:
            if not letter.isalpha():
                progress.append(letter)
            elif letter.lower() in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")
        result = " ".join(progress)
        print(result)
        return result

    def process_guess(self, letter):
        """Procesa una letra ingresada y actualiza el estado del juego."""
        if letter.lower() in self.word.lower():
            self.guessed_letters.append(letter.lower())
            return True
        else:
            self.errors += 1
            return False
    def is_won(self):
        """Devuelve True si se adivinaron todas las letras de la palabra."""
        for letter in self.word:
            if letter.isalpha() and letter.lower() not in self.guessed_letters:
                return False
        return True
