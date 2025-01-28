def potencia(a: int, n: int) -> int:
    '''
    Calcula e devolve a potencia de *a* elevado a *n*.
    tal que a != 0
    
    Exemplo
    >>> potencia(4, 0)
    1
    >>> potencia(2, 1)
    2
    >>> potencia(3, 4)
    81
    >>> potencia(-4, 2)
    16
    >>> potencia(-2, 5)
    -32
    '''
    
    if n == 0:
        return 1
    
    else:
        return a * potencia(a, n - 1)



