import itertools
import random
import time


def calcularIndexIACartaElegida(cartasJugadorIA):
    # Obtener las cartas posibles para la mesa
    cartasPosibles = obtenerCartasValidasParaMesa()

    # Filtrar las cartasJugadorIA y quedarse con solo las presentes en cartasPosibles
    cartasJugadorIAPosibles = list(filter(lambda x: x in cartasPosibles, cartasJugadorIA))

    # Si no hay cartas posibles, entonces elige pasar (-1)
    if not cartasJugadorIAPosibles:
        return -1

    # Obtener un elemento al azar de cartas posibles
    cartaElegidaIA = random.choice(cartasJugadorIAPosibles)
    # Obtiene el índice de la carta elegida en la lista completa de cartas del jugador
    return cartasJugadorIA.index(cartaElegidaIA)


def obtenerCartasValidasParaMesa():
    cartasPosibles = []

    for palo in palosCartas:
        # Obtengo las cartas pertenecientes a "palo"
        cartasDePalo = list(filter(lambda x: getPaloCarta(x) == palo, cartasEnMesa))

        # Si no hay ninguna carta de ese palo, solo se puede poner 7
        if not cartasDePalo:
            cartasPosibles.append(("7", palo))
        # Si solo el 7 está puesto, solo se puede poner el 6
        elif len(cartasDePalo) == 1 and getValorCarta(cartasDePalo[0]) == '7':
            cartasPosibles.append(("6", palo))
        # En cualquier otro caso, está puesto el 6, el 7, y quizá más cartas
        else:
            # Ordenar la lista por valor (el palo es igual siempre)
            cartasDePalo = sorted(cartasDePalo, key=funcionOrdenamientoPorValor)

            # Obtener carta de menor valor (primera en lista ordenada)
            menorCarta = cartasDePalo[0]
            # Si la menor carta no es la primera (A)
            if not getValorCarta(menorCarta) == 'A':
                indexValorMenorCarta = valoresCartas.index(getValorCarta(menorCarta))
                cartasPosibles.append((valoresCartas[indexValorMenorCarta - 1], palo))

            # Obtener carta de mayor valor (última en lista ordenada)
            mayorCarta = cartasDePalo[len(cartasDePalo) - 1]
            # Si la mayor carta no es la última (K)
            if not getValorCarta(mayorCarta) == 'K':
                indexValorMayorCarta = valoresCartas.index(getValorCarta(mayorCarta))
                cartasPosibles.append((valoresCartas[indexValorMayorCarta + 1], palo))
    return cartasPosibles


# Gets an input number from the user within min and max value INCLUSIVE
def obtenerInputNumeroEntreValores(nombreValor, minValue, maxValue):
    if minValue > maxValue:
        print("ERROR: minValue debe ser menor a maxValue")
        return 0

    inputValue = 0

    while True:
        error = False
        try:
            inputValue = int(input('Ingrese %s: ' % nombreValor))
            if not minValue <= inputValue <= maxValue:
                error = True
        except ValueError:
            error = True

        if error:
            print("Numero erróneo, debe ser un numero entre %d y %d." % (minValue, maxValue))
        else:
            break

    return inputValue


def obtenerInputString(nombreValor):
    while True:
        inputValue = input('Ingrese %s: ' % nombreValor)

        # Hacer un trim, y verificar que no sea string vacío
        inputValue = inputValue.strip()

        if not inputValue:
            print("No puede ser vacío")
        else:
            return inputValue


def funcionOrdenamientoPorPaloYValor(_carta):
    # Ordenar primero por palo, luego por numero, ascendente
    palo = getPaloCarta(_carta)
    indexPalo = palosCartas.index(palo)

    valor = getValorCarta(_carta)
    indexValor = valoresCartas.index(valor)
    return indexPalo * 100 + indexValor


def funcionOrdenamientoPorValor(_carta):
    # Ordenar solo por valor (no tener en cuenta palo)
    return valoresCartas.index(getValorCarta(_carta))


def ordenarCartas(_listaCartas):
    return sorted(_listaCartas, key=funcionOrdenamientoPorPaloYValor)


def printListaCartas(_listaCartas, withIndex=False):
    for _i in range(len(_listaCartas)):
        if withIndex:
            print('%d: %s' % (_i, toLongString(_listaCartas[_i])))
        else:
            print('%s' % (toLongString(_listaCartas[_i])))


def getValorCarta(_carta):
    return _carta[0]


def getPaloCarta(_carta):
    return _carta[1]


def getPaloCartaLargo(_carta):
    return palosCartasLargo[palosCartas.index(getPaloCarta(_carta))]


def toShortString(_carta):
    return getValorCarta(_carta) + getPaloCarta(_carta)


def toLongString(_carta):
    return getValorCarta(_carta) + ' de ' + getPaloCartaLargo(_carta)


def getPlayerName(_playerData):
    return _playerData[0]


def getPlayerIsIA(_playerData):
    return _playerData[1]


# Valores de las cartas y palos
valoresCartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# D = Diamante, C = Corazon, P = Picas, T = Trébol
palosCartas = ['D', 'C', 'P', 'T']
palosCartasLargo = ['Diamante', 'Corazon', 'Picas', 'Trébol']

# Mazo
mazo = list(itertools.product(valoresCartas, palosCartas))
random.shuffle(mazo)
cantidadCartasTotales = len(mazo)

# Elegir cantidad de jugadores, debe ser entre cantidadMinimaJugadores y cantidadMaximaJugadores
cantidadMinimaJugadores = 3
cantidadMaximaJugadores = 5
cantidadJugadores = 3
# cantidadJugadores = obtenerInputNumeroEntreValores("la cantidad de jugadores",
#                                                    cantidadMinimaJugadores,
#                                                    cantidadMaximaJugadores)
playerData = []

# Crear lista de cartas por jugador
# Cada elemento en esta lista es una lista de las cartas de dicho jugador
cartasPorJugador = []
cartasEnMesa = []

cartasPorJugador.append([])
cartasPorJugador.append([])
cartasPorJugador.append([])
playerData.append(("Nachiten", False))
playerData.append(("JessiBot", True))
playerData.append(("PedroBot", True))

# Crear la lista de cartas, nombre y IA de cada jugador
# for indexJugador in range(cantidadJugadores):
#     cartasPorJugador.append([])
#
#     nombreJugador = obtenerInputString("el nombre del jugador %d" % (indexJugador + 1))
#     esIAJugador = obtenerInputNumeroEntreValores("si el jugador %d es IA (1) o Humano (0)" % (indexJugador + 1), 0, 1)
#
#     esIaJugadorBool = True if esIAJugador == 1 else False
#
#     playerData.append((nombreJugador, esIaJugadorBool))

# Repartir las cartas
for indexCarta in range(cantidadCartasTotales):
    indexJugador = indexCarta % cantidadJugadores
    cartasPorJugador[indexJugador].append(mazo.pop())

contadorTurnoJugador = 0

while True:
    indiceTurnoJugador = contadorTurnoJugador % cantidadJugadores
    cantidadCartasJugador = len(cartasPorJugador[indiceTurnoJugador])

    # Ordenar cartas del jugador
    cartasPorJugador[indiceTurnoJugador] = ordenarCartas(cartasPorJugador[indiceTurnoJugador])

    while True:
        # Ordenar la mesa
        cartasEnMesa = ordenarCartas(cartasEnMesa)

        # Mostrar la mesa
        print("Las cartas en la mesa son: ")
        printListaCartas(cartasEnMesa)

        playerEsIA = getPlayerIsIA(playerData[indiceTurnoJugador])
        indiceCartaElegida = None

        if playerEsIA:
            # Se muestran las cartas de quien le toca jugar con índice
            print('[Turno de: %s (%s)] Eligiendo de forma automática...' % (
                getPlayerName(playerData[indiceTurnoJugador]),
                'IA' if playerEsIA else 'Humano'))
            print("Cartas en la mano de la IA:")
            printListaCartas(cartasPorJugador[indiceTurnoJugador], True)

            # Esperar 3 segundos
            time.sleep(2)

            # Calcular de forma automática el índice de carta elegida
            indiceCartaElegida = calcularIndexIACartaElegida(cartasPorJugador[indiceTurnoJugador])
        else:
            # Se muestran las cartas de quien le toca jugar con índice
            print('[Turno de: %s (%s)] Elija que carta jugar. Sus %d cartas son:' % (
                getPlayerName(playerData[indiceTurnoJugador]),
                'IA' if playerEsIA else 'Humano',
                cantidadCartasJugador))
            printListaCartas(cartasPorJugador[indiceTurnoJugador], True)

            # Pedir un index de la carta elegida, verificar que esté entre 0 y cantidadCartasJugador
            # Volver a pedir el índice mientras no sea válido
            indiceCartaElegida = obtenerInputNumeroEntreValores('el numero de la carta que desea jugar (-1 para pasar)',
                                                                -1,
                                                                cantidadCartasJugador - 1)

        # Validar que sea correcto insertar esta carta
        cartasValidas = obtenerCartasValidasParaMesa()

        # Elige pasar, entonces se corta el while
        if indiceCartaElegida == -1:
            # Si tiene alguna carta en su mano válida en la mesa, entonces no puede pasar
            tieneCartaValidaEnMano = any(item in cartasValidas for item in cartasPorJugador[indiceTurnoJugador])

            if tieneCartaValidaEnMano:
                print("No puede pasar, debe jugar una carta.")
                print("Las cartas posibles para jugar son: ")
                printListaCartas(cartasValidas)
                continue
            break

        cartaElegida = cartasPorJugador[indiceTurnoJugador][indiceCartaElegida]

        # Validar que la carta elegida sea válida para poner en la mesa
        if cartaElegida in cartasValidas:
            # Quitar la carta de la mano del jugador y ponerla en la mesa
            cartasEnMesa.append(cartasPorJugador[indiceTurnoJugador].pop(indiceCartaElegida))
            break
        else:
            print("No se puede jugar esa carta, elija otra")
            print("Las cartas posibles para jugar son: ")
            printListaCartas(cartasValidas)

    # Incrementar turno
    contadorTurnoJugador += 1
