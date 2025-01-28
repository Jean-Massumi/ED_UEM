def tem_impar(lst_num: list[int]) -> bool:
    '''
    Devolve True se algum dos elementos de *lst_num* for ímpar, False caso contrário.
    
    Exemplo
    >>> tem_impar([2, 4, 8, 16, 32])
    False
    >>> tem_impar([1, 3, 5])
    True
    >>> tem_impar([66, 30, 3, 44, 68])
    True
    >>> tem_impar([0, 4, 4, 14, 33])
    True
    '''
    def _tem_impar(lst_num: list[int], tam: int) -> bool:
        if tam == len(lst_num):
            return False
        
        else:
            return (lst_num[tam] % 2 != 0) or _tem_impar(lst_num, tam + 1)
        
    return _tem_impar(lst_num, 0)

















