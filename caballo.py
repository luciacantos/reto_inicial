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

# ejemplo
n = 10
resultado = contar_movimientos(n)
print(f"La cantidad de movimientos posibles para {n} es {resultado}")
