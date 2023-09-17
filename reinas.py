def seguro(tablero, fila, columna):
    n = len(tablero)
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    for i, j in zip(range(fila, -1, -1), range(columna, n)):
        if tablero[i][j] == 1:
            return False
    return True

def soluciones(n, fila=0, tablero=None):
    if tablero is None:
        tablero = [[0]*n for _ in range(n)]

    if fila == n:
        return 1

    total = 0

    for columna in range(n):
        if seguro(tablero, fila, columna):
            tablero[fila][columna] = 1
            total += soluciones(n, fila + 1, tablero)
            tablero[fila][columna] = 0
    return total

# tabla para los resultados
valores_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]
print("n\tSoluciones")
print("-" * 20)

for n in valores_n:
    resultado = soluciones(n)
    print(f"{n}\t{resultado}")
