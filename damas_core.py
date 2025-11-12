import numpy as np

VACIA = 0
P_J1 = 1
R_J1 = 2
P_J2 = 3
R_J2 = 4

def crear_tablero():
    tablero = np.zeros((8, 8), dtype=int)
    # Peones jugador 1
    for f in range(5, 8):
        for c in range(8):
            if (f + c) % 2 == 1:
                tablero[f, c] = P_J1
    # Peones jugador 2
    for f in range(3):
        for c in range(8):
            if (f + c) % 2 == 1:
                tablero[f, c] = P_J2
    return tablero

def mostrar_tablero(tablero):
    simbolos = {VACIA: ".", P_J1: "o", R_J1: "O", P_J2: "x", R_J2: "X"}
    print("  0 1 2 3 4 5 6 7")
    for i in range(8):
        fila = [simbolos[x] for x in tablero[i]]
        print(i, " ".join(fila))

def movimiento_valido(tablero, f1, c1, f2, c2, jugador):
    if not (0 <= f2 < 8 and 0 <= c2 < 8):
        return False
    pieza = tablero[f1, c1]
    destino = tablero[f2, c2]
    if destino != VACIA:
        return False

    df = f2 - f1
    dc = abs(c2 - c1)
    if pieza == P_J1:
        return df == -1 and dc == 1
    elif pieza == P_J2:
        return df == 1 and dc == 1
    elif pieza in (R_J1, R_J2):
        return abs(df) == 1 and dc == 1
    return False

def mover(tablero, f1, c1, f2, c2):
    pieza = tablero[f1, c1]
    tablero[f1, c1] = VACIA
    tablero[f2, c2] = pieza
    if pieza == P_J1 and f2 == 0:
        tablero[f2, c2] = R_J1
    elif pieza == P_J2 and f2 == 7:
        tablero[f2, c2] = R_J2

def hay_captura(tablero, f1, c1, jugador):
    pieza = tablero[f1, c1]
    direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for df, dc in direcciones:
        f2, c2 = f1 + df, c1 + dc
        f3, c3 = f1 + 2*df, c1 + 2*dc
        if 0 <= f3 < 8 and 0 <= c3 < 8:
            medio = tablero[f2, c2]
            destino = tablero[f3, c3]
            if destino == VACIA and medio != VACIA:
                if jugador == 1 and medio in (P_J2, R_J2) and pieza in (P_J1, R_J1):
                    return True
                if jugador == 2 and medio in (P_J1, R_J1) and pieza in (P_J2, R_J2):
                    return True
    return False

def capturar(tablero, f1, c1, f2, c2):
    df = (f2 - f1) // 2
    dc = (c2 - c1) // 2
    tablero[f1 + df, c1 + dc] = VACIA
    mover(tablero, f1, c1, f2, c2)

def hay_movimientos(tablero, jugador):
    for f in range(8):
        for c in range(8):
            pieza = tablero[f, c]
            if (jugador == 1 and pieza in (P_J1, R_J1)) or (jugador == 2 and pieza in (P_J2, R_J2)):
                if hay_captura(tablero, f, c, jugador):
                    return True
                for df in (-1, 1):
                    for dc in (-1, 1):
                        f2, c2 = f + df, c + dc
                        if movimiento_valido(tablero, f, c, f2, c2, jugador):
                            return True
    return False


def pedir_jugada():
    try:
        f1 = int(input("Escribe la fila de la ficha que quieres mover: "))
        c1 = int(input("Escribe la columna de la ficha que quieres mover: "))
        f2 = int(input("Escribe la fila a donde quieres mover tu ficha escogida: "))
        c2 = int(input("Escribe la columna a donde quieres mover tu ficha escogida: "))
        return f1, c1, f2, c2
    except:
        print("Eso no se puede , sorry :( ")
        return None
