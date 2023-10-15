import itertools
import random


def funcionOrdenamiento(_carta):
    # Ordenar primero por palo, luego por numero, ascendente
    palo = getShortPalo(_carta)
    indexPalo = palosCartasCorto.index(palo)

    valor = getValor(_carta)
    indexValor = valoresCartas.index(valor)
    return indexPalo * 100 + indexValor


def ordenarCartas(_listaCartas):
    return sorted(_listaCartas, key=funcionOrdenamiento)


def printListaCartas(_listaCartas, withIndex=False):
    for _i in range(len(_listaCartas)):
        if withIndex:
            print('%d: %s' % (_i, toLongString(_listaCartas[_i])))
        else:
            print('%s' % (toLongString(_listaCartas[_i])))


def getValor(_carta):
    return _carta[0]


def getShortPalo(_carta):
    return _carta[1]


def getPaloLong(_carta):
    return palosCartasLargo[palosCartasCorto.index(getShortPalo(_carta))]


def toShortString(_carta):
    return getValor(_carta) + getShortPalo(_carta)


def toLongString(_carta):
    return getValor(_carta) + ' de ' + getPaloLong(_carta)


valoresCartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# D = Diamante, C = Corazon, P = Picas, T = Trébol
palosCartasCorto = ['D', 'C', 'P', 'T']
palosCartasLargo = ['Diamante', 'Corazon', 'Picas', 'Trébol']

mazo = list(itertools.product(valoresCartas, palosCartasCorto))

random.shuffle(mazo)

# printListaCartas(mazo)

# Elegir cantidad de jugadores, debe ser número entre 3 y 5
cantidadJugadores = 0

while True:
    error = False
    try:
        cantidadJugadores = int(input('Ingrese cantidad de jugadores: '))
        if not 3 <= cantidadJugadores <= 5:
            error = True
    except ValueError:
        error = True

    if error:
        print("Numero erróneo, debe ser un numero entre 3 y 5.")
    else:
        break

# Crear lista de cartas por jugador
# Cada elemento en esta lista es una lista de las cartas de dicho jugador
cartasPorJugador = []
cartasEnLaMesa = []

cantidadCartas = len(mazo)

# Crear la lista de cartas de cada jugador
for i in range(cantidadJugadores):
    cartasPorJugador.append([])

# Repartir las cartas
for i in range(cantidadCartas):
    indexJugador = i % cantidadJugadores
    cartasPorJugador[indexJugador].append(mazo.pop())

indiceTurnoJugador = 0
cantidadCartasJugador = len(cartasPorJugador[indiceTurnoJugador])
cartasJugador = cartasPorJugador[indiceTurnoJugador]

# Ordenar cartas del jugador
cartasJugador = ordenarCartas(cartasJugador)

# El primer jugador es el humano, mostrarle sus cartas y hacerlo elegir una con un index
print('[Es su turno] Elija que carta jugar. Sus cartas son:')
printListaCartas(cartasJugador, True)

indiceCartaElegida = -1

# Pedir un index de la carta elegida, verificar que esté entre 0 y cantidadCartasJugador
# Volver a pedir el índice mientras no sea válido
while True:
    indiceCartaElegida = int(input('Ingrese el numero de la carta que desea jugar: '))
    if not (cantidadCartasJugador > indiceCartaElegida >= 0):
        print('ERROR: El numero de carta ingresado no es valido')
    else:
        break

# Quitar la carta de la mano del jugador y ponerla en la mesa
cartasEnLaMesa.append(cartasPorJugador[indiceTurnoJugador].pop(indiceCartaElegida))
