import random

class Truco:
    def __init__(self):
        self.lista_numeros = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        self.lista_palos = ['Espada', 'Basto', 'Copa', 'Oro']
        self.valor_cartas = {
            '1 de Espada': 15,
            '1 de Basto': 14,
            '7 de Espada': 13,
            '7 de Oro': 12,
            '3 de Espada': 11,
            '3 de Basto': 11,
            '3 de Copa': 11,
            '3 de Oro': 11,
            '2 de Espada': 10,
            '2 de Basto': 10,
            '2 de Copa': 10,
            '2 de Oro': 10,
            '1 de Copa': 9,
            '1 de Oro': 8,
            '12 de Espada': 7,
            '12 de Basto': 7,
            '12 de Copa': 7,
            '12 de Oro': 7,
            '11 de Espada': 6,
            '11 de Basto': 6,
            '11 de Copa': 6,
            '11 de Oro': 6,
            '10 de Espada': 5,
            '10 de Basto': 5,
            '10 de Copa': 5,
            '10 de Oro': 5,
            '7 de Copa': 4,
            '7 de Basto': 3,
            '6 de Espada': 2,
            '6 de Basto': 2,
            '6 de Copa': 2,
            '6 de Oro': 2,
            '5 de Espada': 1,
            '5 de Basto': 1,
            '5 de Copa': 1,
            '5 de Oro': 1,
            '4 de Espada': 0,
            '4 de Basto': 0,
            '4 de Copa': 0,
            '4 de Oro': 0
        }
        self.mazo_cartas = self.crear_mazo()
        self.barajar_mazo()

    def crear_mazo(self):
        mazo = []
        for numero in self.lista_numeros:
            for palo in self.lista_palos:
                mazo.append(numero + ' de ' + palo)
        return mazo

    def barajar_mazo(self):
        random.shuffle(self.mazo_cartas)

    def repartir_cartas(self):
        jugador1_cartas = []
        computadora_cartas = []
        for i in range(6):  # Se reparten 6 cartas en total (3 para cada jugador)
            if i % 2 == 0:  # Jugador 1 recibe carta
                jugador1_cartas.append(self.mazo_cartas.pop(0))  # Pop desde el principio de la lista
            else:  # La computadora recibe carta
                computadora_cartas.append(self.mazo_cartas.pop(0))  # Pop desde el principio de la lista
        return jugador1_cartas, computadora_cartas

    def mostrar_mazo(self):
        for carta in self.mazo_cartas:
            print(carta)

    def determinar_primero(self):
        return random.choice(['Jugador 1', 'Computadora'])

    def jugar_carta(self, jugador, cartas):
        if jugador == 'Jugador 1':
            print("Turno de Jugador 1:")
            print("Cartas disponibles:")
            for i, carta in enumerate(cartas):
                print(f"{i + 1}: {carta}")
            indice_carta = int(input("Seleccione el número de la carta que desea jugar: ")) - 1
            carta_jugada = cartas.pop(indice_carta)
            print(f"Jugador 1 jugó: {carta_jugada}")
            return carta_jugada
        elif jugador == 'Computadora':
            print("Turno de la Computadora:")
            carta_jugada = random.choice(cartas)
            cartas.remove(carta_jugada)
            print(f"La Computadora jugó: {carta_jugada}")  # Imprimir la carta jugada por la computadora
            return carta_jugada

    def comparar_cartas(self, carta_jugador1, carta_computadora):
        valor_jugador1 = self.valor_cartas[carta_jugador1]
        valor_computadora = self.valor_cartas[carta_computadora]
        if valor_jugador1 > valor_computadora:
            print("Jugador 1 gana la jugada.")
            return 'Jugador 1'
        elif valor_jugador1 < valor_computadora:
            print("Computadora gana la jugada.")
            return 'Computadora'
        else:
            print("Empate en esta jugada.")
            return None

# Crear un objeto mazo de cartas
mazo = Truco()

# Repartir cartas intercaladas entre jugador 1 y la computadora
jugador1_cartas, computadora_cartas = mazo.repartir_cartas()

# Determinar quién es el primero en jugar
primer_jugador = mazo.determinar_primero()
print(f"{primer_jugador} es mano.")

# Mostrar las cartas de jugador 1 y la computadora
print("\nCartas del jugador 1:")
for carta in jugador1_cartas:
    print(carta)
print("\nCartas de la computadora:")
for carta in computadora_cartas:
    print(carta)

puntos_jugador1 = 0
puntos_computadora = 0

# Realizar tres rondas
for ronda in range(3):
    # Jugar una carta según el turno del jugador
    carta_jugada_jugador1 = mazo.jugar_carta(primer_jugador, jugador1_cartas if primer_jugador == 'Jugador 1' else computadora_cartas)
    carta_jugada_computadora = mazo.jugar_carta('Computadora', computadora_cartas)

    # Comparar cartas y determinar ganador de la ronda
    ganador_ronda = mazo.comparar_cartas(carta_jugada_jugador1, carta_jugada_computadora)

    # Actualizar puntos
    if ganador_ronda == 'Jugador 1':
        puntos_jugador1 += 1
    elif ganador_ronda == 'Computadora':
        puntos_computadora += 1

    # Determinar siguiente jugador para la próxima ronda
    if ganador_ronda:
        primer_jugador = ganador_ronda
    else:
        primer_jugador = primer_jugador

# Determinar el ganador de la mano
if puntos_jugador1 > puntos_computadora:
    print
