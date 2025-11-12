import damas_core

def main():
    tablero = damas_core.crear_tablero()
    jugador = 1
    fin = False
    while not fin:
        damas_core.mostrar_tablero(tablero)
        print(f"\nLe toca al jugador {jugador}")

        if not damas_core.hay_movimientos(tablero, jugador):
            print(f"Jugador {3 - jugador} gana, {jugador} no puede mover")
            fin = True
        else:
            jugada_valida = False
            jugada = damas_core.pedir_jugada()
            if jugada is not None:
                f1, c1, f2, c2 = jugada
                pieza = tablero[f1, c1]
                if (jugador == 1 and pieza not in (damas_core.P_J1, damas_core.R_J1)) or (jugador == 2 and pieza not in (damas_core.P_J2, damas_core.R_J2)):
                    print("Esa no es tu pieza , no toques")
                else:
                    if damas_core.hay_captura(tablero, f1, c1, jugador):
                        df, dc = (f2 - f1), (c2 - c1)
                        if abs(df) == 2 and abs(dc) == 2:
                            medio = tablero[f1 + df//2, c1 + dc//2]
                            if (jugador == 1 and medio in (damas_core.P_J2, damas_core.R_J2)) or (jugador == 2 and medio in (damas_core.P_J1, damas_core.R_J1)):
                                damas_core.capturar(tablero, f1, c1, f2, c2)
                                jugada_valida = True
                            else:
                                print("No se puede capturar esa pieza , chaval que haces")
                        else:
                            print("Puedes capturar una pieza : ) , pero tienes que poner la siguente casilla diagonal a esa")
                    elif damas_core.movimiento_valido(tablero, f1, c1, f2, c2, jugador):
                        damas_core.mover(tablero, f1, c1, f2, c2)
                        jugada_valida = True
                    else:
                        print("Eso no se puede hacer , CRACK")
            else:
                print("NOP")
            if jugada_valida:
                if jugador == 1:
                    jugador = 2
                else:
                    jugador = 1

if __name__ == "__main__":
    main()
