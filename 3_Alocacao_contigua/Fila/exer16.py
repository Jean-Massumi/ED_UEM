from fila_arranjo_fim import Fila as FilaF
from fila_arranjo_inicio_fim import Fila as FilaIF


def operacoes(fila: FilaF | FilaIF, n: int):
    '''
    Inserie os elementos '1', '2', ..., 'n' em *fila*
    e depois esvazia *fila*.
    '''
    
    for num in range(1, (n + 1)):
        fila.enfileira(str(num))
        
    while (fila.vazia()):
        fila.desenfileira()
    


def main():
    from timeit import timeit
    for fila in ['FilaF', 'FilaIF']:
        print(fila)
        for n in [100000, 400000, 1000000]:
            tempo = timeit(f'operacoes({fila}(), {n})',
                           setup=f'from __main__ import operacoes, {fila}',
                           number=10)
            print(n, tempo)


if __name__ == '__main__':
    main()
