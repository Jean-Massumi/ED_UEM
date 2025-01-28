def qtd_vezes(lst: list[int], val: int) -> int:
    '''
    Devolve quantas vezes o *val* apareceu em *lst*.
    
    Exemplo
    >>> qtd_vezes([], 7) is None
    0
    >>> qtd_vezes([1, 2, 3, 4], 7)
    0
    >>> qtd_vezes([12, 8, 23], 23)
    1
    >>> qtd_vezes([1, 2, 3, 1, 1], 1)
    3
    >>> qtd_vezes([-14, 5, 9, -14, 26], -14)
    2
    '''

    def _qtd_vezes(lst: list[int], inicio: int, val: int):
        if inicio == len(lst):
            return 0
        
        else:
            if lst[inicio] == val:
                return 1 + _qtd_vezes(lst, (inicio + 1), val)
            
            else:
                return _qtd_vezes(lst, (inicio + 1), val)

    return _qtd_vezes(lst, 0, val)











