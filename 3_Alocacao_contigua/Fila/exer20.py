import time
from collections import deque

def teste_tempo_deque(n: int):
    """Testa o tempo de execução do método popleft de collections.deque."""
    fila_deque = deque(range(n))  # Inicializa o deque com n elementos
    inicio = time.time()
    while fila_deque:
        fila_deque.popleft()
    fim = time.time()
    return fim - inicio

def teste_tempo_list(n: int):
    """Testa o tempo de execução do método pop(0) de uma lista."""
    fila_list = list(range(n))  # Inicializa a lista com n elementos
    inicio = time.time()
    while fila_list:
        fila_list.pop(0)
    fim = time.time()
    return fim - inicio

def main():
    n = 100000  # Número de elementos para teste

    print(f"Testando com {n} elementos...\n")

    tempo_deque = teste_tempo_deque(n)
    print(f"Tempo com collections.deque (popleft): {tempo_deque:.6f} segundos")

    tempo_list = teste_tempo_list(n)
    print(f"Tempo com list (pop(0)): {tempo_list:.6f} segundos")

    diferenca = tempo_list - tempo_deque
    print(f"\nDiferença de tempo: {diferenca:.6f} segundos")
    print(f"O método popleft do deque foi {tempo_list / tempo_deque:.2f} vezes mais rápido.")

if __name__ == "__main__":
    main()

if __name__ == '__main__':
    main()
