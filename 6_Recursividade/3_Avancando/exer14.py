def nao_decrescente(lst: list[int]) -> bool:
    '''
    Devolve True se *lst* está em ordem não decrescente.
    
    Exemplo
    >>> nao_decrescente([])
    True
    >>> nao_decrescente([2])
    True
    >>> nao_decrescente([2, 2, 2, 2])
    True
    >>> nao_decrescente([1, 2, 2, 4])
    True
    >>> nao_decrescente([6, 7, 8, 9])
    True
    >>> nao_decrescente([7, 5, 3, 1])
    False
    >>> nao_decrescente([1, 2, -4, 7])
    False
    >>> nao_decrescente([5, 7, 10, 2])
    False
    '''
     
    def _nao_decrescente(lst: list[int], inicio: int) -> bool:
        if len(lst) <= 1:
            return True
        
        elif inicio == len(lst) - 1:
            return True
        
        else:
            return lst[inicio] <= lst[inicio + 1] and _nao_decrescente(lst, inicio + 1)

    return _nao_decrescente(lst, 0)


