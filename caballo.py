caso_base = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]

def contar_movimientos(n):
    def dfs(pos, moves):
        if moves == 0:
            return 1
        count = 0
        for neighbor in caso_base[pos]:
            count += dfs(neighbor, moves - 1)
        return count

    movimientos = 0

    for position in range(10):
        movimientos += dfs(position, n)
    return movimientos


# Crear una tabla para mostrar los resultados

valores_de_n = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]

print("n\tPosibilidades válidas")
print("-" * 20)

for n in valores_de_n:
    resultado = contar_movimientos(n)
    print(f"{n}\t{resultado}")
