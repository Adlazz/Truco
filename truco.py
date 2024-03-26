import random

class MazoDeCartas:
    def __init__(self):
        self.lista_numeros = ['1', '2', '3', '4', '5', '6', '7', '10', '11', '12']
        self.lista_palos = ['Espada', 'Basto', 'Copa', 'Oro']
        self.valor_cartas = self.crear_valor_cartas()
        self.mazo_cartas = self.crear_mazo()
        self.barajar_mazo()

    def crear_valor_cartas(self):
        valor_cartas = {}
        cartas_especiales = {
            '1 de Espada': 15,
            '1 de Basto': 14,
            '7 de Espada': 13,
            '7 de Oro': 12,
            '3': 11,
            '2': 10,
            '1 de Copa': 9,
            '1 de Oro': 8,
            '12': 7,
            '11': 6,
            '10': 5,
            '7 de Copa': 4,
            '7 de Basto': 3,
            '6': 2,
            '5': 1,
            '4': 0
            }
        for numero in self.lista_numeros:
            for palo in self.lista_palos:
                carta = numero + ' de ' + palo
                if carta in cartas_especiales:
                    valor_cartas[carta] = cartas_especiales[carta]
                elif numero in cartas_especiales:
                    valor_cartas[carta] = cartas_especiales[numero]
        return valor_cartas

    def imprimir_carta_y_valor(self, carta):
        print(f"Carta: {carta}, Valor: {self.valor_cartas[carta]}")

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




mazo = MazoDeCartas()
mazo.imprimir_carta_y_valor('2 de Espada')