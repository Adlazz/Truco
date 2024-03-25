import random

class MazoDeCartas:
    def __init__(self):
        self.lista_numeros = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        self.lista_palos = ['Espada', 'Basto', 'Copa', 'Oro']
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

# Crear un objeto mazo de cartas
mazo = MazoDeCartas()

# Repartir cartas intercaladas entre jugador 1 y la computadora
jugador1_cartas, computadora_cartas = mazo.repartir_cartas()

# Mostrar las cartas de jugador 1
print("Cartas del jugador 1:")
for carta in jugador1_cartas:
    print(carta)

# Mostrar las cartas de la computadora
print("\nCartas de la computadora:")
for carta in computadora_cartas:
    print(carta)
