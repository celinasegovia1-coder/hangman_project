# Hangman Project - Juego del Ahorcado

## Descripción

Proyecto académico desarrollado en Python que consiste en implementar un juego de Ahorcado mediante consola.

El proyecto se desarrolló de forma progresiva, siguiendo las ocho tareas establecidas en la consigna académica.

## Equipo de desarrollo

- Celina Segovia
- Eduardo Rodríguez
- Fabriccio Ferreira

## Tecnologías

- Python
- Git
- GitHub
- Visual Studio Code

## Requisitos

- Python 3 instalado

## Cómo ejecutar

Desde la carpeta del proyecto:

    python main.py

## Cómo se juega

- El programa elige al azar una película de wordlist.txt y la muestra oculta con guiones bajos.
- En cada turno se ingresa una letra. Solo se aceptan letras; los números, símbolos y letras ya intentadas se rechazan.
- Si la letra está en la palabra, se revela en todas sus posiciones. Si no está, se suma un error.
- Los espacios y signos de puntuación se muestran automáticamente.
- Se gana al adivinar todas las letras y se pierde al llegar a 6 errores.
- Al terminar, el juego pregunta si se quiere jugar de nuevo (s/n).

## Estructura del proyecto

- main.py: punto de entrada del programa y bucle del juego.
- game.py: clase HangmanGame con el estado y la lógica del juego.
- utils.py: funciones auxiliares, como get_random_word().
- wordlist.txt: listado de palabras posibles.
- README.md: documentación del proyecto.

## Funcionalidades adicionales

- Permite iniciar una nueva partida al finalizar la anterior.
- Acepta respuestas afirmativas (s, si, sí) y negativas (n, no).
- Valida las respuestas y vuelve a preguntar cuando son incorrectas.

## Estado del desarrollo

Tareas 0 a 7: implementación completa.

Tarea 8: mejora opcional: funcionalidad de volver a jugar implementada y probada.
