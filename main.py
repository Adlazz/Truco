# JUEGO TRUCO 

import random

# Definir el mazo de cartas con su valor correspondiente
cartas = {
    'Espada 1': 14, 'Espada 7': 12, 'Espada 3': 10, 'Espada 2': 9, 'Espada 12': 7, 'Espada 11': 6, 'Espada 10': 5, 'Espada 6': 3, 'Espada 5': 2, 'Espada 4': 1,
    'Oro 7': 11, 'Oro 3': 10, 'Oro 2': 9, 'Oro 1': 8, 'Oro 12': 7, 'Oro 11': 6, 'Oro 10': 5, 'Oro 6': 3, 'Oro 5': 2, 'Oro 4': 1,
    'Copa 3': 10, 'Copa 2': 9, 'Copa 1': 8, 'Copa 12': 7, 'Copa 11': 6, 'Copa 10': 5, 'Copa 7': 4, 'Copa 6': 3, 'Copa 5': 2, 'Copa 4': 1,
    'Basto 1': 13, 'Basto 3': 10, 'Basto 2': 9, 'Basto 12': 7, 'Basto 11': 6, 'Basto 10': 5, 'Basto 7': 4, 'Basto 6': 3, 'Basto 5': 2, 'Basto 4': 1
}

# Función para mostrar las cartas del jugador
def mostrar_cartas(nombre_jugador, cartas_jugador):
    print("\nCartas de", nombre_jugador + ":")
    for i, carta in enumerate(cartas_jugador, start=1):
        print(f"{i}. {carta}")

# Función para que la computadora elija una carta aleatoria
def elegir_carta_computadora(cartas_computadora):
    return random.choice(cartas_computadora)

# Función principal del juego
def jugar_truco():
    # Repartir cartas al jugador y a la computadora
    cartas_jugador = dict(random.sample(cartas.items(), 3))
    cartas_computadora = dict(random.sample(cartas.items(), 3))
    
    # Mostrar las cartas del jugador
    mostrar_cartas("Jugador", cartas_jugador)
    
    # Turno de la computadora
    carta_computadora = elegir_carta_computadora(cartas_computadora)
    print("\nLa computadora juega:", carta_computadora)
    
    # Turno del jugador
    while True:
        try:
            indice_carta = int(input("\nElige el número de la carta que quieres jugar (1-3): ")) - 1
            if indice_carta < 0 or indice_carta > 2:
                raise ValueError
            carta_jugador = cartas_jugador.pop(indice_carta)
            break
        except (ValueError, IndexError):
            print("Selección inválida. Introduce un número entre 1 y 3.")
    
    print("Has jugado:", carta_jugador)
    
    # Determinar el ganador
    if cartas.index(carta_jugador) > cartas.index(carta_computadora):
        print("\n¡Ganaste!")
    elif cartas.index(carta_jugador) < cartas.index(carta_computadora):
        print("\n¡La computadora gana!")
    else:
        print("\nEmpate.")
def bienvenida():
    print("¡Bienvenido al juego de Truco!")
    nombre_jugador = input("Por favor, introduce tu nombre: ")
    print(f"\nHola {nombre_jugador}! Vamos a comenzar.\n")

# Llamar a la función de bienvenida antes de iniciar el juego
bienvenida()

# Iniciar el juego
jugar_truco()